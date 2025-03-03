from pdfminer.high_level import extract_text
import os
from fastapi import UploadFile
import openai

openai.api_key = "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" # Put in .env file during production.

def gpt_skills_summary(extracted_text: str) -> str:

    system_prompt = (
        "You are an AI that summarizes a list of useful skills from an academic transcript for use in a student's resume'.\n"
        "Given the following extract from an academic transcript, identify the key skills related to the modules the student has studied.\n"
        "Please provide only the skills, as a comma-separated list. Do not include the module names or course codes in the response.\n"
        "(The extracted text from the transcript follows below.)"
    )
    user_prompt = extracted_text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=100,
            temperature=0.0
        )
        
        # Extract the skills summary from the response
        skills_summary = response['choices'][0]['message']['content'].strip()
        return skills_summary

    except Exception as e:
        # Return error message as a JSON-like string
        return f'{{"error": "Error calling GPT: {str(e)}"}}'

async def parse_transcript_pdf(transcript: UploadFile) -> str:
    temp_filename = f"temp_{transcript.filename}"
    with open(temp_filename, "wb") as buffer:
        buffer.write(await transcript.read())

    # Extract text using pdfminer
    extracted_text = extract_text(temp_filename)

    # Delete the temporary file
    os.remove(temp_filename)

    skills_summary = gpt_skills_summary(extracted_text)

    return skills_summary