import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(prompt: str, chat_history=[]):
    response = model.generate_content(
        chat_history + [{"role": "user", "parts": [prompt]}]
    )
    return response.text
