import openai
import ffmpeg
import os
from app.models.video import Video  # Adjust import if necessary
from pydub import AudioSegment

openai.api_key = 'YOUR_API_KEY'

def extract_audio_from_video(video_path: str):
    audio_path = f"{video_path}.mp3"
    try:
        # Use ffmpeg or pydub to extract audio
        audio = AudioSegment.from_file(video_path)
        audio.export(audio_path, format="mp3")
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
    prompt = f"Analyze the following text for grammar, fluency, and coherence. Provide feedback on improvements:\n\n{text}"
    try:
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
    except Exception as e:
        raise Exception(f"Error analyzing text with GPT-4: {str(e)}")

def process_video(video_path: str):
    try:
        # Step 1: Extract audio from video
        audio_path = extract_audio_from_video(video_path)

        # Step 2: Transcribe audio to text using Whisper API
        transcript = transcribe_audio(audio_path)

        # Step 3: Analyze the transcribed text with GPT-4
        analysis_result = analyze_text_with_gpt(transcript)

        # Output the results (could be saved to a DB or returned in a response)
        print("Transcription:", transcript)
        print("GPT-4 Analysis:", analysis_result)

        # Clean up audio file after processing
        os.remove(audio_path)

    except Exception as e:
        print(f"Error processing video: {str(e)}")
