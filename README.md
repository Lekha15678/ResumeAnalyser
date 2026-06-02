# Resume Analyzer

An AI-powered Resume Analyzer built using Python, Flask, Machine Learning, and NLP.

## Overview

Resume Analyzer helps users evaluate their resumes by extracting skills, predicting career categories, calculating industry readiness scores, and providing personalized improvement suggestions.

The application supports multiple file formats and offers ATS-style resume analysis to help candidates improve their job applications.

---

## Features

### Resume Upload
Supports:

- PDF (.pdf)
- Word Documents (.docx)
- Text Files (.txt)
- Images (.jpg, .jpeg, .png)

### Skill Extraction
Automatically detects technical skills from uploaded resumes.

Example:

- Python
- SQL
- AWS
- Power BI
- Pandas
- NumPy
- Machine Learning

### Resume Category Prediction

Predicts the most suitable career category such as:

- Data Science
- Python Developer
- Web Developer
- Java Developer
- Testing
- HR

### Industry Readiness Score

Evaluates resume quality based on:

- Skills
- Projects
- Certifications
- Internship Experience
- GitHub Profile
- LinkedIn Profile
- Soft Skills

### ATS Compatibility Analysis

Shows:

- ATS Match Score
- Matched Skills
- Missing Skills

### Personalized Suggestions

Provides improvement recommendations along with learning resources.

---

## Technologies Used

### Backend

- Python
- Flask

### Machine Learning

- Scikit-Learn
- TF-IDF Vectorizer
- Naive Bayes Classification

### NLP

- NLTK

### Resume Processing

- PyPDF2
- python-docx
- Pillow
- Pytesseract OCR

### Frontend

- HTML
- CSS

---

## Project Structure

```text
ResumeAnalyser/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── utils/
│   ├── parser.py
│   ├── predictor.py
│   ├── skill_extract.py
│   ├── analyzer.py
│   └── job_match.py
│
└── dataset/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/resumeanalyser.git
```

### Open Project

```bash
cd resumeanalyser
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Future Enhancements

- AI Resume Suggestions
- Resume PDF Report Generation
- Job Description Matching
- Resume Ranking System
- User Login System
- Resume History Tracking
- Cloud Deployment

---

## Author

Lekha Pandharipande

B.Tech Computer Science and Engineering (Data Science)

St. Vincent Pallotti College of Engineering and Technology, Nagpur

LinkedIn:
https://www.linkedin.com/in/lekha-pandharipande-3267b928b/

---

## License

This project is developed for educational and learning purposes.
