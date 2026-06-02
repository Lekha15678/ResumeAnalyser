from utils.parser import extract_resume

from utils.skill_extract import extract_skills

file = open(

    "resume.pdf",

    "rb"

)

text = extract_resume(

    file

)

skills = extract_skills(

    text

)

print(

    skills

)
