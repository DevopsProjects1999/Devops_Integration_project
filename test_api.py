import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "http://localhost",  # Use your domain if needed
    "X-Title": "GenAI-Tutor",
    "Content-Type": "application/json"
}

payload = {
    "model": "mistralai/mistral-7b-instruct",
    "messages": [
        {"role": "user", "content": "Explain what is a Linux kernel."}
    ]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)
