import openai
import ffmpeg
import os
import cv2
import numpy as np
import dotenv
import io
import mediapipe as mp
from app.models.video import Video  # Adjust import if necessary
from pydub import AudioSegment

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

mp_holistic = mp.solutions.holistic


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


def transcribe_audio(audio_path: str):
    try:
        with open(audio_path, 'rb') as audio_file:
            transcript = openai.Audio.transcribe(
                model="whisper-1", file=audio_file
            )
        return transcript['text']
    except Exception as e:
        raise Exception(f"Error transcribing audio: {str(e)}")


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
                    feedback.append(analyze_frame_with_gpt(image_bytes))
            
            frame_count += 1
        
        cap.release()
        os.remove(video_path)
        
        return feedback
    except Exception as e:
        raise Exception(f"Error analyzing body language: {str(e)}")


def analyze_frame_with_gpt(image_bytes: bytes):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=[
                {"role": "system", "content": "You are an AI that analyzes interview body language, including facial expressions, posture, and hand gestures."},
                {"role": "user", "content": "Analyze this interview frame for confidence, engagement, and clarity."},
                {"role": "user", "content": image_bytes}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error analyzing frame with GPT-4 Vision: {str(e)}"


def process_video(video_bytes: bytes):
    try:
        audio_path = extract_audio_from_video(video_bytes)
        transcript = transcribe_audio(audio_path)
        analysis_result = analyze_text_with_gpt(transcript)
        body_language_feedback = analyze_body_language(video_bytes)
        
        result = {
            "transcript": transcript,
            "text_analysis": analysis_result,
            "body_language_feedback": body_language_feedback
        }
        
        os.remove(audio_path)
        return result
    except Exception as e:
        os.remove(audio_path)
        print(f"Error processing video: {str(e)}")
