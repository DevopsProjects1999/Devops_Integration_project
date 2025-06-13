# genai-tutor/app/tutor.py
import openai
import logging
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
logger = logging.getLogger(__name__)


def explain_concept(topic: str, question: str) -> str:
    prompt = f"Explain the following {topic} concept in simple terms: {question}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"OpenAI API call failed: {e}")
        return "Sorry, I couldn't fetch an explanation at the moment."

