import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rank_resume(resume: str, job_description: str) -> dict:
    prompt = (
        f"Compare the resume to the job description and give a match score from 0-100 "
        f"with a brief reason. Output JSON like {{'score': int, 'feedback': str}}.\n\n"
        f"Resume:\n{resume}\n\nJob Description:\n{job_description}"
    )
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    message = response.choices[0].message.content
    return eval(message)
