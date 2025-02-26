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
import dotenv
from tqdm import tqdm
import asyncio
import logging
import tempfile
import time
import random

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Suppress specific TensorFlow warnings
warnings.filterwarnings("ignore", category=UserWarning, module='tensorflow')
warnings.filterwarnings("ignore", category=DeprecationWarning, module='tensorflow')

# MediaPipe setup
mp_pose = mp.solutions.pose
mp_face_mesh = mp.solutions.face_mesh
mp_holistic = mp.solutions.holistic


def retry_with_backoff(func, *args, **kwargs):
    retries = 5
    delay = 2  # initial delay in seconds
    for _ in range(retries):
        try:
            return func(*args, **kwargs)
        except openai.error.RateLimitError:
            # Handle rate limit error gracefully
            logging.warning("Rate limit reached, retrying after wait...")
            time.sleep(delay)
            delay *= random.uniform(1.1, 1.5)  # Increase delay with each retry
        except openai.error.InvalidRequestError as e:
            # Handle token limit exceeded errors or other invalid request errors
            if 'context length' in str(e):
                logging.warning("Token limit exceeded, reducing the length of messages and retrying.")
                # Optionally, you could attempt to split the input into smaller chunks here.
            else:
                logging.error(f"Invalid request error: {e}")
            time.sleep(delay)
            delay *= random.uniform(1.1, 1.5)  # Increase delay with each retry
    raise Exception("Rate limit exceeded after retries or invalid request error occurred")


def extract_audio_from_video(video_bytes: bytes):
    try:
        logging.info(f"Received video bytes of size: {len(video_bytes)} bytes")

        if len(video_bytes) == 0:
            raise ValueError("Received video bytes are empty.")

        # Create a temporary video file to store video bytes
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video_file:
            temp_video_file.write(video_bytes)
            temp_video_path = temp_video_file.name
            logging.info(f"Temporary video file created: {temp_video_path}")
        
        time.sleep(3)  # Wait for the system to ensure the file is fully written
        
        if not os.path.exists(temp_video_path) or os.path.getsize(temp_video_path) == 0:
            raise ValueError(f"Error: Video file is not valid or empty: {temp_video_path}")

        # Delete the existing output.mp3 if it exists
        if os.path.exists("output.mp3"):
            os.remove("output.mp3")
            logging.info("Existing output.mp3 deleted.")

        # Use ffmpeg to extract the audio
        audio_path = "output.mp3"
        process = (
            ffmpeg
            .input(temp_video_path)
            .output(audio_path, format="mp3", acodec="libmp3lame", ar=44100, ac=2, ab="192k")
            .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True, quiet=False)
        )
        
        process.wait()  # Wait for the process to complete
        
        stderr = process.stderr.read()
        if stderr:
            logging.error(f"FFmpeg stderr: {stderr.decode()}")
        
        os.remove(temp_video_path)  # Remove the temporary video file
        
        if os.path.exists(audio_path):
            logging.info(f"Audio extracted successfully: {audio_path}")
            return audio_path
        else:
            raise Exception("Audio extraction failed. Output file not created.")
    
    except Exception as e:
        logging.error(f"Error extracting audio: {str(e)}")
        raise


def transcribe_audio(audio_path: str):
    try:
        with open(audio_path, 'rb') as audio_file:
            transcript = openai.Audio.transcribe(
                model="whisper-1", file=audio_file
            )
        return transcript.get('text', '')
    except Exception as e:
        logging.error(f"Error transcribing audio: {str(e)}")
        raise


def analyze_text_with_gpt(text: str):
    prompt = f"The following text is a mock interview. Analyze it for grammar, fluency, and coherence. Provide feedback in bullet points:\n\n{text}"
    try:
        response = retry_with_backoff(openai.ChatCompletion.create,
                                      model="gpt-4",
                                      messages=[{"role": "system", "content": "You are an AI that helps improve interview content."},
                                                {"role": "user", "content": prompt}],
                                      max_tokens=500,
                                      temperature=0.7)
        return response.choices[0].message['content']
    except openai.error.RateLimitError:
        logging.warning("Rate limit exceeded during GPT analysis. Please try again later.")
        return "Error: Rate limit exceeded. Please try again later."
    except openai.error.InvalidRequestError as e:
        logging.warning("Token limit exceeded or invalid request during GPT analysis.")
        return "Error: Message too long. Please try to shorten your input and try again."
    except Exception as e:
        logging.error(f"Error analyzing text with GPT-4: {str(e)}")
        return f"Error: {str(e)}"


def analyze_body_pose(image_bytes):
    try:
        nparr = np.frombuffer(image_bytes, np.uint8)  # Convert bytes to numpy array
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # Decode to image
        
        if image is None:
            raise ValueError("Could not decode image.")
        
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                body_parts = [f"Part {i}: {part}" for i, part in enumerate(results.pose_landmarks.landmark)]
                return "\n".join(body_parts)
            return "No body detected"
    except Exception as e:
        logging.error(f"Error analyzing body pose: {str(e)}")
        return f"Error analyzing body pose: {str(e)}"


def analyze_emotion(image_bytes):
    try:
        nparr = np.frombuffer(image_bytes, np.uint8)  # Convert bytes to numpy array
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # Decode to image
        
        if image is None:
            raise ValueError("Could not decode image.")
        
        result = DeepFace.analyze(image, actions=['emotion'])
        dominant_emotion = result[0]['dominant_emotion']
        return f"Dominant Emotion: {dominant_emotion}"
    except Exception as e:
        logging.error(f"Error analyzing emotion: {str(e)}")
        return f"Error analyzing emotion: {str(e)}"


def get_summary_feedback_batch(body_analyses, emotion_analyses):
    try:
        feedback_input = "Body Pose Analysis:\n" + "\n".join(body_analyses) + "\n\nEmotion Analysis:\n" + "\n".join(emotion_analyses)

        response = retry_with_backoff(openai.ChatCompletion.create,
                                      model="gpt-4",
                                      messages=[{
                                          "role": "system", "content": "You are an interview assistant that provides feedback on public speaking, including body language, facial expressions, and emotions."
                                      }, {
                                          "role": "user", "content": f"Provide a summary of feedback based on the following analyses in point form, suggest things to improve on:\n{feedback_input}"
                                      }],
                                      max_tokens=500,
                                      temperature=0.7)

        return response.choices[0].message["content"]
    except openai.error.RateLimitError:
        logging.warning("Rate limit exceeded during feedback generation. Please try again later.")
        return "Error: Rate limit exceeded. Please try again later."
    except openai.error.InvalidRequestError as e:
        logging.warning("Token limit exceeded or invalid request during feedback generation.")
        return "Error: Message too long. Please try to shorten your input and try again."
    except Exception as e:
        logging.error(f"Error generating feedback: {str(e)}")
        return f"Error generating feedback: {str(e)}"


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
        logging.error(f"Error analyzing body language: {str(e)}")
        raise


def process_video(video_bytes: bytes, feedback_queue: list):
    audio_path = None
    try:
        logging.info("Started processing video...")

        # Extract audio
        try:
            audio_path = extract_audio_from_video(video_bytes)
            logging.info(f"Audio extracted: {audio_path}")
            feedback_queue.append(f"Audio extracted successfully: {audio_path}")
        except Exception as e:
            logging.error(f"Error extracting audio: {str(e)}")
            feedback_queue.append(f"Error extracting audio: {str(e)}")
            return {"success": False, "message": f"Error extracting audio: {str(e)}"}

        # Transcribe audio
        try:
            transcript = transcribe_audio(audio_path)
            logging.info(f"Transcription complete: {transcript}")
            feedback_queue.append(f"Transcription complete: {transcript}")
        except Exception as e:
            logging.error(f"Error transcribing audio: {str(e)}")
            feedback_queue.append(f"Error transcribing audio: {str(e)}")
            return {"success": False, "message": f"Error transcribing audio: {str(e)}"}

        # Analyze body language
        try:
            body_language_feedback = analyze_body_language(video_bytes)
            logging.info(f"Body language feedback: {body_language_feedback}")
            feedback_queue.append(f"Body language feedback: {body_language_feedback}")
        except Exception as e:
            logging.error(f"Error analyzing body language: {str(e)}")
            feedback_queue.append(f"Error analyzing body language: {str(e)}")
            return {"success": False, "message": f"Error analyzing body language: {str(e)}"}

        return {"success": True, "feedback": feedback_queue}

    except Exception as e:
        logging.error(f"An error occurred during video processing: {str(e)}")
        feedback_queue.append(f"An error occurred: {str(e)}")
        return {"success": False, "message": f"An error occurred: {str(e)}"}
