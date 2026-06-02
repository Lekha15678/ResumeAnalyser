import re

def match_resume_with_jd(resume_text, jd_text):

    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    words = re.findall(r'\w+', jd_text)

    keywords = list(set(words))

    matched = []
    missing = []

    for word in keywords:

        if len(word) < 4:
            continue

        if word in resume_text:

            matched.append(word)

        else:

            missing.append(word)

    total = len(matched) + len(missing)

    if total == 0:

        score = 0

    else:

        score = int(

            len(matched) / total * 100

        )

    return score, matched, missing