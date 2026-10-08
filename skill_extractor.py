import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s+]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text

def extract_skills(resume_text, skills_list):
    found_skills = []

    for skill in skills_list:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, resume_text):
            found_skills.append(skill)

    return sorted(list(set(found_skills)))