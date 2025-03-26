# app/services/resume_service.py
import io
import openai
import json
from pdfminer.high_level import extract_text

# If you're using openai==0.28.0, the older ChatCompletion syntax works
openai.api_key = "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"  # Or read from env in production

def split_text_into_chunks(text: str, max_chars=5000):
    """
    Splits the resume text into chunks of <= max_chars characters
    to avoid token or length limits when calling GPT.
    """
    lines = text.splitlines()
    chunks = []
    current_chunk = []
    current_length = 0

    for line in lines:
        if (current_length + len(line)) > max_chars:
            # finalize the current chunk
            chunks.append("\n".join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(line)
        current_length += len(line)

    # flush the last chunk
    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks

def merge_contact(original_contact, new_contact):
    """
    Merges contact subfields: Name, Email, Phone.
    If new_contact has them non-empty, override original.
    """
    for key in ["Name", "Email", "Phone"]:
        if key in new_contact and new_contact[key]:
            original_contact[key] = new_contact[key]
    return original_contact

def ask_gpt_for_resume_info(chunk_text: str, chunk_index=1) -> str:
    """
    Calls GPT with openai==0.28.0 / ChatCompletion.
    Asks for 6 headings: contact, education, workExperience, skills, certifications, hobbies.
    Returns raw JSON string from GPT.
    """
    system_prompt = (
        "You are an AI that extracts structured information from a resume. "
        "Output valid JSON with exactly six keys:\n"
        "1) 'contact' (Name, Email, Phone)\n"
        "2) 'education' (array)\n"
        "3) 'workExperience' (array)\n"
        "4) 'skills' (array)\n"
        "5) 'certifications' (array)\n"
        "6) 'hobbies' (array)\n"
        "If something isn't found, use an empty array or null.\n"
        f"(Chunk {chunk_index} of the resume text follows below.)"
    )

    user_prompt = chunk_text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=1200,
            temperature=0.0
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f'{{"error": "Error calling GPT: {str(e)}"}}'

def merge_gpt_results(chunks):
    """
    For each chunk, call GPT, parse partial JSON, merge into final 6 headings.
    """
    final_json = {
        "contact": {"Name": None, "Email": None, "Phone": None},
        "education": [],
        "workExperience": [],
        "skills": [],
        "certifications": [],
        "hobbies": []
    }

    for i, chunk_text in enumerate(chunks, start=1):
        partial_json_str = ask_gpt_for_resume_info(chunk_text, i)
        try:
            partial_data = json.loads(partial_json_str)
        except json.JSONDecodeError:
            # GPT returned invalid JSON or an error
            continue

        # Merge contact subfields
        final_json["contact"] = merge_contact(
            final_json["contact"], partial_data.get("contact", {})
        )
        # Extend arrays
        final_json["education"] += partial_data.get("education", [])
        final_json["workExperience"] += partial_data.get("workExperience", [])
        final_json["skills"] += partial_data.get("skills", [])
        final_json["certifications"] += partial_data.get("certifications", [])
        final_json["hobbies"] += partial_data.get("hobbies", [])

    return final_json

def parse_resume_pdf_bytes(pdf_bytes: bytes) -> dict:
    """
    1) Extract text in-memory from PDF bytes
    2) Split into chunks
    3) Call GPT for each chunk, merge partial results
    4) Return final JSON dict
    """
    if not pdf_bytes:
        raise ValueError("No PDF data provided.")

    # Extract text with pdfminer
    try:
        pdf_text = extract_text(io.BytesIO(pdf_bytes))
    except Exception as e:
        raise ValueError(f"Error parsing PDF: {str(e)}")

    if not pdf_text.strip():
        raise ValueError("PDF text extraction yielded nothing.")

    # Split the text to avoid token limit
    chunks = split_text_into_chunks(pdf_text, max_chars=5000)
    final_data = merge_gpt_results(chunks)
    return final_data