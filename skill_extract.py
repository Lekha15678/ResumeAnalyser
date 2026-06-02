skills_db = [

    "python",
    "sql",
    "machine learning",
    "data science",
    "flask",
    "html",
    "css",
    "javascript",
    "power bi",
    "numpy",
    "pandas",
    "nltk",
    "aws",
    "data analysis",
    "data visualization",
    "excel",
    "matplotlib"

]

def extract_skills(text):

    found = []

    text = text.lower()

    for skill in skills_db:

        if skill in text:

            found.append(skill)

    return found