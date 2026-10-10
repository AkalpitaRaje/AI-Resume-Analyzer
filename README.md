AI Resume Analyzer & Job Recommendation System
An AI-powered web application that analyzes resumes, evaluates ATS compatibility, identifies missing skills, and recommends relevant job opportunities based on the candidate's profile.

Project Overview
The AI Resume Analyzer & Job Recommendation System is designed to help job seekers understand how well their resume matches a job profile.

The application extracts information from uploaded resumes, analyzes skills and keywords, calculates an ATS-style score, identifies missing skills, and provides job recommendations using Natural Language Processing techniques.

Key Features
Upload resumes in PDF and DOCX formats
Extract and process resume text
Identify technical and professional skills
Calculate an ATS-style resume score
Identify missing or relevant skills
Recommend suitable job opportunities
Display analysis results through an interactive dashboard
Generate resume analysis reports
Store and manage analysis history using SQLite
User signup and login functionality
Technologies Used
Python
Streamlit
Pandas
SQLite
Natural Language Processing (NLP)
TF-IDF
Cosine Similarity
Matplotlib

Project Structure
AI-Resume-Analyzer/
│
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── ats_score.py
├── job_recommender.py
├── report_generator.py
├── pdf_report_generator.py
├── database.py
│
├── skills.csv
├── jobs.csv
├── requirements.txt
├── README.md
└── .gitignore

How It Works
User creates an account and logs into the application.
User uploads a resume in PDF or DOCX format.
The system extracts text and relevant information from the resume.
Skills and keywords are identified from the extracted content.
The resume is evaluated against job-related requirements.
An ATS-style score and missing skills are displayed.
TF-IDF and Cosine Similarity are used to identify relevant job recommendations.
The application presents the analysis through an interactive dashboard.
Analysis history can be stored and managed by the user.
Learning Outcomes

Through this project, I developed practical experience in:

Python application development
Data processing with Pandas
Natural Language Processing
Text similarity techniques
Database management using SQLite
Streamlit application development
Data visualization
Resume and ATS analysis concepts
Future Enhancements
Integration with live job portals
Advanced resume parsing
Machine learning-based job recommendations
Resume improvement suggestions
Cloud deployment and API integration
Author

Akalpita Raje

MCA Graduate | Aspiring Data Analyst