# app/routes.py
from flask import Blueprint, request, render_template
from app.tutor import generate_explanation

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    explanation = None
    if request.method == "POST":
        question = request.form.get("question")
        explanation = generate_explanation(question)
    return render_template("index.html", explanation=explanation)
