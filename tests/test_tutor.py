# genai-tutor/tests/test_tutor.py
from app.tutor import explain_concept

def test_explain_concept(monkeypatch):
    class MockResponse:
        choices = [type("obj", (object,), {"message": type("msg", (object,), {"content": "This is a mock explanation."})()})()]

    monkeypatch.setattr("openai.ChatCompletion.create", lambda *args, **kwargs: MockResponse())
    result = explain_concept("Python", "What is a lambda function?")
    assert "mock explanation" in result
