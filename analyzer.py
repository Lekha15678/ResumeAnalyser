def resume_score(text):

    score = 0
    suggestions = []

    text = text.lower()

    # =====================
    # Technical Skills
    # =====================

    skills = [

        "python",
        "sql",
        "aws",
        "machine learning",
        "data analysis",
        "power bi",
        "excel",
        "pandas",
        "numpy",
        "matplotlib",
        "tableau",
        "tensorflow",
        "scikit-learn",
        "deep learning",
        "statistics"

    ]

    found_skills = 0

    for skill in skills:

        if skill in text:

            found_skills += 1

    score += min(found_skills * 3, 30)

    # =====================
    # Projects
    # =====================

    if "project" in text:

        score += 15

    else:

        suggestions.append({

            "title": "Add More Projects",

            "link": "https://www.kaggle.com/datasets"

        })

    # =====================
    # Internship
    # =====================

    if "internship" in text:

        score += 15

    else:

        suggestions.append({

            "title": "Add Internship Experience",

            "link": "https://internshala.com/"

        })

    # =====================
    # Certifications
    # =====================

    if "certificate" in text or "certification" in text:

        score += 10

    else:

        suggestions.append({

            "title": "Earn Industry Certifications",

            "link": "https://www.coursera.org/"

        })

    # =====================
    # GitHub
    # =====================

    if "github" in text:

        score += 10

    else:

        suggestions.append({

            "title": "Create GitHub Portfolio",

            "link": "https://github.com/"

        })

    # =====================
    # LinkedIn
    # =====================

    if "linkedin" in text:

        score += 5

    else:

        suggestions.append({

            "title": "Build LinkedIn Profile",

            "link": "https://www.linkedin.com/"

        })

    # =====================
    # Resume Length
    # =====================

    words = len(text.split())

    if words > 200:

        score += 10

    else:

        suggestions.append({

            "title": "Improve Resume Content",

            "link": "https://www.overleaf.com/latex/templates/tagged/cv"

        })

    # =====================
    # Soft Skills
    # =====================

    soft_skills = [

        "communication",
        "leadership",
        "teamwork",
        "problem solving",
        "collaboration",
        "presentation"

    ]

    found_soft = False

    for skill in soft_skills:

        if skill in text:

            found_soft = True
            break

    if found_soft:

        score += 10

    else:

        suggestions.append({

            "title": "Add Soft Skills Section",

            "link": "https://www.indeed.com/career-advice/career-development/soft-skills"

        })

    # =====================
    # Education
    # =====================

    if "b.tech" in text or "bachelor" in text:

        score += 5

    # =====================
    # Final Score
    # =====================

    if score > 100:

        score = 100

    return score, suggestions