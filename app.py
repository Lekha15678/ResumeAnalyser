from flask import *

from utils.parser import extract_resume
from utils.skill_extract import extract_skills
from utils.predictor import predict_resume
from utils.analyzer import resume_score
from utils.job_match import match_resume_with_jd

app = Flask(__name__)


@app.route('/')
def home():

    return render_template(
        "index.html"
    )


@app.route('/analyze', methods=['POST'])
def analyze():

    file = request.files['resume']

    text = extract_resume(file)

    if not text.strip():

        return "Could not read file"

    skills = extract_skills(text)

    category = predict_resume(text)

    score, suggestions = resume_score(text)

    # Get Job Description
    jd = request.form.get(
        "job_description",
        ""
    )

    # ATS Match Score
    match_score = 0
    matched = []
    missing = []

    if jd.strip():

        match_score, matched, missing = (
            match_resume_with_jd(
                text,
                jd
            )
        )

    return render_template(

        "result.html",

        skills=skills,

        category=category,

        score=score,

        suggestions=suggestions,

        match_score=match_score,

        matched=matched,

        missing=missing

    )


if __name__ == "__main__":

    app.run(
        debug=True
    )