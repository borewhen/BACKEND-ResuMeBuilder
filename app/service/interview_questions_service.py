# app/services/gpt_service.py
import openai

openai.api_key = "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"  # Replace with your actual API key, consider loading this from environment variables for security
'''
def generate_initial_questions(resume_data: dict) -> list:
    """
    Generates a list of initial interview questions based on the detailed resume data using the OpenAI Chat API.
    """
    prompt = f"Generate five interview questions based on these resume details: {resume_data}"
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Specify the correct chat model
        messages=[{"role": "system", "content": prompt}],  # Set up a system message with the prompt
        max_tokens=500
    )
    questions = response['choices'][0]['message']['content'].strip().split('\n')
    return questions

def generate_dynamic_question(previous_question: str, answer: str, resume_data: dict) -> str:
    """
    Generates a follow-up question based on the previous question, user's answer, and detailed resume information using the OpenAI Chat API.
    """
    prompt = f"Given the previous question '{previous_question}', the answer '{answer}', and the detailed resume information {resume_data}, generate a follow-up question. So if the answer '{answer}' is sufficient and clear then generate some other questions related to the resume {resume_data}. If the answer '{answer}'is not clear or sufficient then dive deeper in the answer '{answer}' "
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt}
        ],
        max_tokens=200
    )
    follow_up_question = response['choices'][0]['message']['content'].strip()
    return follow_up_question
'''
def generate_questions_based_on_context(prompt, initial=False):
    """
    Generates questions or follow-up questions based on the provided prompt.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Or use the latest available model
        messages=[{"role": "system", "content": prompt}],
        max_tokens=500 if initial else 200  # Adjust token limit based on needs
    )
    return response['choices'][0]['message']['content'].strip()
