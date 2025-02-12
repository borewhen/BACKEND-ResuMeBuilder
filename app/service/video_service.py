import openai
import ffmpeg
import os
from app.models.video import Video  # Adjust import if necessary
from pydub import AudioSegment
import dotenv
import io

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_audio_from_video(video_bytes: bytes):
    audio_path = f"output.mp3"
    try:
        # Use ffmpeg or pydub to extract audio
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
    prompt = f"Analyze the following text for grammar, fluency, and coherence. Provide feedback on improvements:\n\n{text}"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an AI that helps improving people's interview content."},
                      {"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        
        print(response)
        
        return response.choices[0].message.content
    
    except Exception as e:
        raise Exception(f"Error analyzing text with GPT-4: {str(e)}")

def process_video(video_bytes: bytes):
    try:
        # Step 1: Extract audio from video
        audio_path = extract_audio_from_video(video_bytes)

        # Step 2: Transcribe audio to text using Whisper API
        transcript = transcribe_audio(audio_path)
        
        # Step 3: Analyze the transcribed text with GPT-4
        analysis_result = analyze_text_with_gpt(transcript)
        
        # Output the results (could be saved to a DB or returned in a response)
        result = {
            "transcript": transcript,
            "analysis": analysis_result
        }
        print(result)
        # Clean up audio file after processing
        os.remove(audio_path)
        
        return result

    except Exception as e:
        print(f"Error processing video: {str(e)}")
        os.remove(audio_path)
