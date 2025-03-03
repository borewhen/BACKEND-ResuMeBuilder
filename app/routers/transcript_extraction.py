from fastapi import APIRouter, File, UploadFile
from app.service.transcript_extraction_service import parse_transcript_pdf

router = APIRouter()

@router.post("/upload-transcript/")
async def upload_transcript(transcript: UploadFile = File(...)):
    if not transcript.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        skills_summary = await parse_transcript_pdf(transcript)
        return {"skills": skills_summary}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unhandled error: {str(e)}")