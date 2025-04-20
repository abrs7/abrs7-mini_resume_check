import os
from openai import OpenAI
from dotenv import load_dotenv
import json
import google.generativeai as genai



load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if os.getenv("GEMINI_API_KEY"):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
else:
    gemini_model = None


def clean_json_like_text(text: str) -> str:
    import re
    cleaned = re.sub(r"```(?:json)?", "", text)
    cleaned = cleaned.replace("```", "").strip()
    return cleaned


def rank_resume(
        resume: str, 
        job_description: str,
        model: str = "gemini-1.5-flash",
        provider: str = "gemini",
        custom_prompt: str | None = None
) -> dict:
    if not resume or not job_description:
        return {"score": 0, "feedback": "Missing resume or job description."}
    prompt = custom_prompt  or (
        f"Compare the resume to the job description and give a match score from 0-100 "
        f"with a brief reason. Output JSON like {{'score': int, 'feedback': str}}.\n\n"
        f"Resume:\n{resume}\n\nJob Description:\n{job_description}"
    )
    
    try:
        if provider.lower() == "openai":
            response = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
    
            message = response.choices[0].message.content
        elif provider.lower() == "gemini":
            if not gemini_model:
                raise ValueError("Gemini API key not configured.")
            response = gemini_model.generate_content(prompt)
            message = response.text 
        else:
            raise ValueError(f"Unsupported provider: {provider}")
        cleaned_message = clean_json_like_text(message)
        try:
            return json.loads(cleaned_message)
        except json.JSONDecodeError as err:
            return {"score": 0, "feedback": f"Could not parse response: {cleaned_message}"}


    except Exception as e:
        return {"score": 0, "feedback": f"Error from {provider}: {str(e)}"}       
