from pydantic import BaseModel

# Define Pydantic model for request body
class AnswerRequest(BaseModel):
    answer: str
