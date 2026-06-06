# Resume Analyzer

A Flask-based web application that analyzes resumes using Machine Learning and Natural Language Processing (NLP).

The application predicts the resume category, extracts skills, calculates ATS Match Score, evaluates industry readiness, and provides personalized improvement suggestions.

---

## Overview

Resume Analyzer helps job seekers evaluate their resumes against industry standards. It identifies skills, predicts career domains, measures ATS compatibility, and suggests improvements to increase employability.

---

## Features

- Resume Category Prediction
- Skill Extraction
- ATS Match Score Calculation
- Industry Readiness Score
- Missing Skill Detection
- Resume Improvement Suggestions
- PDF Resume Upload
- Responsive User Interface

---

## Problem Statement

Many candidates submit resumes without understanding whether they meet industry expectations or Applicant Tracking System (ATS) requirements.

This project helps users:

- Analyze resume quality
- Identify missing skills
- Improve ATS compatibility
- Measure industry readiness
- Access learning resources for improvement

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Flask | Web Framework |
| HTML | Frontend Structure |
| CSS | User Interface Styling |
| Scikit-learn | Machine Learning |
| Pandas | Data Processing |
| NLTK | Natural Language Processing |
| PyPDF2 | PDF Text Extraction |
| Joblib | Model Serialization |

---

## Project Structure

```text
ResumeAnalyzer/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── css/
│       └── style.css
│
├── uploads/
│
├── utils/
│   ├── parser.py
│   ├── predictor.py
│   ├── skill_extract.py
│   ├── analyzer.py
│   └── job_match.py
│
└── requirements.txt
```

---

## Project Workflow

### 1. Resume Upload
The user uploads a PDF resume.

### 2. Text Extraction
Text is extracted from the uploaded resume.

### 3. Resume Classification
The trained machine learning model predicts the resume category.

Example categories:

- Data Science
- Web Development
- HR
- Testing
- Java Developer

### 4. Skill Extraction
Relevant technical and professional skills are identified.

### 5. ATS Analysis
Resume skills are compared against job requirements.

### 6. Score Generation
Industry Readiness Score and ATS Match Score are calculated.

### 7. Suggestions
Personalized recommendations are provided for improvement.

---

## Sample Output

### Resume Category
Data Science

### Industry Readiness Score
82%

### ATS Match Score
75%

### Detected Skills

- Python
- SQL
- Pandas
- NumPy
- Power BI
- AWS

### Suggestions

- Add Internship Experience
- Improve Project Descriptions
- Earn Industry Certifications
- Create a GitHub Portfolio

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/resumeanalyser.git
```

### Navigate to Project Folder

```bash
cd resumeanalyser
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## Usage

1. Open the application in a browser.
2. Upload a resume in PDF format.
3. View the analysis report.
4. Review ATS score, detected skills, and improvement suggestions.

---

## Future Enhancements

- LinkedIn Profile Analysis
- Job Recommendation System
- Resume Ranking System
- AI-Based Resume Suggestions
- Multi-Language Resume Support

---

## Screenshots

### Home Page

Add screenshot here.

### Analysis Report

Add screenshot here.

---

## Author

**Lekha Pandharipande**

B.Tech Data Science Engineering

St. Vincent Pallotti College of Engineering and Technology, Nagpur- Pillow
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
