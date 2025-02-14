import openai
import os
import cv2
import ffmpeg
import numpy as np
import mediapipe as mp
from deepface import DeepFace
import warnings
import tensorflow as tf
from pydub import AudioSegment
from app.models.video import Video  # Adjust import if necessary
import dotenv
from tqdm import tqdm

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Suppress specific TensorFlow warnings
warnings.filterwarnings("ignore", category=UserWarning, module='tensorflow')
warnings.filterwarnings("ignore", category=DeprecationWarning, module='tensorflow')

# MediaPipe setup
mp_pose = mp.solutions.pose
mp_face_mesh = mp.solutions.face_mesh
mp_holistic = mp.solutions.holistic

# Function to extract audio from video
def extract_audio_from_video(video_bytes: bytes):
    audio_path = f"output.mp3"
    try:
        process = (
            ffmpeg
            .input("pipe:0")
            .output(audio_path, format="mp3", acodec="libmp3lame", ar=44100, ac=2, ab="192k")
            .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True, quiet=True)
        )
        process.stdin.write(video_bytes)
        process.stdin.close()
        process.wait()
        return audio_path
    except Exception as e:
        raise Exception(f"Error extracting audio: {str(e)}")

# Function to transcribe audio
def transcribe_audio(audio_path: str):
    try:
        with open(audio_path, 'rb') as audio_file:
            transcript = openai.Audio.transcribe(
                model="whisper-1", file=audio_file
            )
        return transcript['text']
    except Exception as e:
        raise Exception(f"Error transcribing audio: {str(e)}")

# Function to analyze text (grammar, fluency, coherence) using GPT
def analyze_text_with_gpt(text: str):
    prompt = f"The following text is a mock interview. Analyze it for grammar, fluency, and coherence. Provide feedback in bullet points:\n\n{text}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an AI that helps improve interview content."},
                      {"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error analyzing text with GPT-4: {str(e)}")

# Function to analyze body pose using MediaPipe
def analyze_body_pose(image_path):
    try:
        image = cv2.imread(image_path)
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                body_parts = [f"Part {i}: {part}" for i, part in enumerate(results.pose_landmarks.landmark)]
                return "\n".join(body_parts)
            else:
                return "No body detected"
    except Exception as e:
        return f"Error analyzing body pose: {str(e)}"

# Function to analyze emotion using DeepFace
def analyze_emotion(image_path):
    try:
        result = DeepFace.analyze(image_path, actions=['emotion'])
        dominant_emotion = result[0]['dominant_emotion']
        return f"Dominant Emotion: {dominant_emotion}"
    except Exception as e:
        return f"Error analyzing emotion: {str(e)}"

# Function to generate feedback for the analysis in a batch
def get_summary_feedback_batch(body_analyses, emotion_analyses):
    try:
        feedback_input = "Body Pose Analysis:\n" + "\n".join(body_analyses) + "\n\nEmotion Analysis:\n" + "\n".join(emotion_analyses)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "system", "content": "You are an interview assistant that provides feedback on public speaking, including body language, facial expressions, and emotions."
            }, {
                "role": "user", "content": f"Provide a summary of feedback based on the following analyses in point form, suggest things to improve on:\n{feedback_input}"
            }],
            max_tokens=500,
            temperature=0.7
        )

        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error generating feedback: {str(e)}"

# Function to analyze body language for all frames
def analyze_body_language(video_bytes: bytes):
    try:
        video_path = "temp_video.mp4"
        with open(video_path, "wb") as f:
            f.write(video_bytes)
        
        cap = cv2.VideoCapture(video_path)
        holistic = mp_holistic.Holistic()
        feedback = []
        frame_count = 0
        frame_interval = 30  # Process every 30 frames
        
        extracted_frames = []
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            if frame_count % frame_interval == 0:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = holistic.process(rgb_frame)
                
                if results.face_landmarks or results.pose_landmarks or results.left_hand_landmarks or results.right_hand_landmarks:
                    _, buffer = cv2.imencode(".jpg", frame)
                    image_bytes = buffer.tobytes()
                    extracted_frames.append(image_bytes)
            
            frame_count += 1
        
        cap.release()
        os.remove(video_path)
        
        # Batch analyze frames
        batch_size = 10
        batch_results = []

        for i in tqdm(range(0, len(extracted_frames), batch_size), desc="Processing frames in batches"):
            batch_frames = extracted_frames[i:i+batch_size]
            
            body_analyses = []
            emotion_analyses = []

            for frame in batch_frames:
                body_analysis = analyze_body_pose(frame)
                emotion_analysis = analyze_emotion(frame)
                
                body_analyses.append(body_analysis)
                emotion_analyses.append(emotion_analysis)
            
            batch_feedback = get_summary_feedback_batch(body_analyses, emotion_analyses)
            batch_results.append(batch_feedback)

        final_summary = "\n".join(batch_results)
        return final_summary
    except Exception as e:
        raise Exception(f"Error analyzing body language: {str(e)}")

# Function to process the video (transcription, body language, feedback)
def process_video(video_bytes: bytes):
    try:
        audio_path = extract_audio_from_video(video_bytes)
        transcript = transcribe_audio(audio_path)
        text_analysis = analyze_text_with_gpt(transcript)
        body_language_feedback = analyze_body_language(video_bytes)
        
        result = {
            "transcript": transcript,
            "text_analysis": text_analysis,
            "body_language_feedback": body_language_feedback
        }
        
        os.remove(audio_path)
        return result
    except Exception as e:
        if os.path.exists(audio_path):
            os.remove(audio_path)
        print(f"Error processing video: {str(e)}")
