# genai-tutor/app/routes.py
from flask import Blueprint, request, render_template
from app.tutor import explain_concept

main = Blueprint('main', __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    explanation = ""
    if request.method == "POST":
        topic = request.form.get("topic")
        question = request.form.get("question")
        explanation = explain_concept(topic, question)
    return render_template("index.html", explanation=explanation)


@main.route("/health")
def health():
    return {"status": "ok"}, 200

