# genai-tutor/app/tutor.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_explanation(question):
    try:
        api_key = os.getenv("OPENROUTER_API_KEY")

        headers = {
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "http://localhost",
            "X-Title": "GenAI-Tutor",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "user", "content": question}
            ]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                 headers=headers, json=payload)

        response.raise_for_status()  # Raise if error

        return response.json()["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"Sorry, I couldn't fetch an explanation at the moment. ({e})"
