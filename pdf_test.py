from utils.parser import extract_resume

file = open(

    "resume.pdf",

    "rb"

)

text = extract_resume(

    file

)

print(text)