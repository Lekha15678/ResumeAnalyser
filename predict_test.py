from utils.parser import extract_resume

from utils.predictor import predict_resume


file = open(

    "resume.pdf",

    "rb"

)


text = extract_resume(

    file

)


category = predict_resume(

    text

)


print(

    category

)