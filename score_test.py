from utils.parser import extract_resume

from utils.analyzer import resume_score

file = open(

    "resume.pdf",

    "rb"

)

text = extract_resume(

    file

)

score,suggestions = resume_score(

    text

)

print(

    score

)

print(

    suggestions

)