# AI Resume Analyzer & Job Recommendation System

An intelligent resume analysis application built using Python, Streamlit, Natural Language Processing (NLP), and SQLite. The system analyzes resumes, evaluates skills against job requirements, generates an ATS-style score, and recommends relevant job opportunities using text similarity techniques.

## Project Overview

The AI Resume Analyzer & Job Recommendation System helps users understand how well their resumes match job requirements. Users can upload resumes in PDF or DOCX format to extract relevant information, identify skills, detect missing skills, and receive suitable job recommendations.

The application combines resume parsing, skill extraction, ATS-style scoring, and text similarity techniques to provide an interactive resume analysis experience.

## Key Features

- **User Authentication:** Account registration and login functionality.
- **Resume Upload:** Supports PDF and DOCX resume formats.
- **Resume Parsing:** Extracts text and relevant information from uploaded resumes.
- **Skill Extraction:** Identifies relevant skills and keywords from resume content.
- **ATS-Style Scoring:** Evaluates resumes against job-related requirements.
- **Skill Gap Analysis:** Highlights missing skills relevant to job requirements.
- **Job Recommendations:** Uses TF-IDF and Cosine Similarity to identify relevant job opportunities.
- **Interactive Dashboard:** Presents analysis results and visualizations.
- **Analysis History:** Allows users to store and manage previous analysis records.
- **Report Generation:** Supports generating analysis reports in TXT and PDF formats.

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Data Processing:** Pandas
- **Natural Language Processing:** NLP
- **Text Similarity:** TF-IDF and Cosine Similarity
- **Database:** SQLite
- **Data Visualization:** Matplotlib
- **File Formats:** PDF, DOCX, TXT, CSV

## Project Structure

```text
AI-Resume-Analyzer/
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── ats_score.py
├── job_recommender.py
├── report_generator.py
├── pdf_report_generator.py
├── database.py
├── skills.csv
├── jobs.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

1. Users create an account and log in to the application.
2. Users upload a resume in PDF or DOCX format.
3. The system extracts text from the uploaded resume.
4. Relevant skills and keywords are identified from the extracted content.
5. The resume is evaluated against job-related requirements.
6. An ATS-style score and missing skills are displayed.
7. TF-IDF and Cosine Similarity are used to identify relevant job recommendations.
8. Analysis results are presented through an interactive dashboard.
9. Users can manage their analysis history and generate reports.

## Learning Outcomes

Through this project, I gained practical experience in:

- Python application development
- Data processing using Pandas
- Natural Language Processing (NLP)
- Text similarity techniques
- Database management using SQLite
- Streamlit application development
- Data visualization
- Resume analysis and ATS concepts

## Future Enhancements

- Integration with live job portals
- Advanced resume parsing
- Machine learning-based job recommendations
- Personalized resume improvement suggestions
- Cloud deployment and API integration

## Author

**Akalpita Raje**

MCA Graduate | Aspiring Data Analyst