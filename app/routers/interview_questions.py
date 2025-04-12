# app/routers/interview_questions.py
from fastapi import APIRouter, HTTPException, Body
from app.service.interview_questions_service import generate_questions_based_on_context # generate_initial_questions, generate_dynamic_question

router = APIRouter()
'''
@router.post("/start-interview")
async def start_interview(resume_data: dict = Body(...)):
    """
    Endpoint to start an interview session and get initial questions based on parsed resume data.
    """
    try:
        questions = generate_initial_questions(resume_data)
        return {"questions": questions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate questions: {str(e)}")

@router.post("/dynamic-follow-up")
async def dynamic_follow_up(data: dict = Body(...)):
    """
    Endpoint to generate a dynamic follow-up or new question based on the previous question, the user's answer, and detailed resume information.
    """
    previous_question = data['previous_question']
    answer = data['answer']
    resume_data = data['resume_data']  # Ensure resume data is passed each time for context
    try:
        follow_up_question = generate_dynamic_question(previous_question, answer, resume_data)
        return {"follow_up_question": follow_up_question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate follow-up question: {str(e)}")
'''
@router.post("/manage-interview")
async def manage_interview(resume_data: dict, previous_question: str = None, answer: str = None):
    """
    Manages an interview session where it either starts the session by generating an initial question based on the resume data,
    or continues by providing a follow-up question based on the previous question and the user's answer.
    """
    try:
        # If there's no previous question, it means this is the start of the interview.
        if not previous_question:
            context = f"Generate starting interview question based on these resume details: {resume_data}"
            first_question = generate_questions_based_on_context(context, initial=True)
            return {"question": first_question}
        else:
            # Generate a follow-up or new question based on the previous interaction
            context = f"Given the previous question '{previous_question}', the answer '{answer}', and the detailed resume information {resume_data}, generate a follow-up or new question. The follow up question will be related to the previous question '{previous_question}' if the answer '{answer}' is unclear, asking for more details. Otherwise ask a seperate question related to the resume information {resume_data}"
            follow_up_question = generate_questions_based_on_context(context)
            return {"question": follow_up_question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to manage interview: {str(e)}")