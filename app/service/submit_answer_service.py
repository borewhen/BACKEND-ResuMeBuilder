# app/services/submit_answer_service.py

from app.models.video_interview_questions import VideoInterviewQuestion
from app.models.users_resume import UsersResume
from sqlalchemy.orm import Session
import openai, json

openai.api_key = "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"

def handle_answer(user_id: int, answer: str, db: Session) -> str:
    current_q = db.query(VideoInterviewQuestion)\
        .filter_by(user_id=user_id, answer=None)\
        .order_by(VideoInterviewQuestion.order)\
        .first()

    if not current_q:
        return "Interview complete!"

    current_q.answer = answer
    db.commit()

    resume_data = db.query(UsersResume).filter_by(user_id=user_id).first()
    resume_json = resume_data.resume_extracted if resume_data else {}

    prompt = f"""
    You are simulating a mock interview session.

    The candidate answered the following question:
    Q: {current_q.question}
    A: {answer}

    Resume Summary: {json.dumps(resume_json)}

    If the answer is clear, detailed, and sufficiently addresses the question, reply with exactly "NEXT".

    Only generate a follow-up if:
    1. The answer lacks depth, OR
    2. Specific techniques, tools, or context are missing from the answer.

    Return just "NEXT" or a follow-up question.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=200
    )

    followup = response["choices"][0]["message"]["content"].strip()

    if followup.lower().startswith("next"):
        next_q = db.query(VideoInterviewQuestion)\
            .filter_by(user_id=user_id, answer=None)\
            .order_by(VideoInterviewQuestion.order)\
            .offset(1).first()
        return next_q.question if next_q else "Interview complete!"
    else:
        new_q = VideoInterviewQuestion(
            user_id=user_id,
            question=followup,
            follow_up=current_q.id,
            order=current_q.order + 0.1
        )
        db.add(new_q)
        db.commit()
        return followup
