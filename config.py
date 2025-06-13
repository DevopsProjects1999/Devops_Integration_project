# genai-tutor/config.py
import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

