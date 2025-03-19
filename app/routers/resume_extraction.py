# app/routers/resume.py
import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.service.resume_extraction_service import parse_resume_pdf_bytes

router = APIRouter()

'''
@router.post("/parse-resume")
async def parse_resume(resume: UploadFile = File(...)):
    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    file_path = os.path.join("uploads", resume.filename)
    with open(file_path, "wb") as f:
        f.write(await resume.read())

    try:
        final_data = parse_resume_pdf(file_path)
    except ValueError as e:
        # e.g. "PDF is empty or unreadable"
        # Cleanup file
        os.remove(file_path)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        os.remove(file_path)
        raise HTTPException(status_code=400, detail=f"Error reading PDF or GPT: {str(e)}")

    # Cleanup
    os.remove(file_path)

    return final_data
'''

@router.post("/parse-resume")
async def parse_resume(resume: UploadFile = File(...)):
    """
    1) Accept a PDF in-memory.
    2) Pass it to parse_resume_pdf_bytes for chunk-based GPT extraction.
    3) Return final JSON.
    """
    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    pdf_bytes = await resume.read()
    if not pdf_bytes:
        raise HTTPException(status_code=400, detail="Empty or unreadable PDF.")

    try:
        final_result = parse_resume_pdf_bytes(pdf_bytes)
        return final_result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unhandled error: {str(e)}")
