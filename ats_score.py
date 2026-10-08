def calculate_ats_score(found_skills, total_skills):
    if total_skills == 0:
        return 0

    score = (len(found_skills) / total_skills) * 100
    return round(score, 2)


def get_missing_skills(found_skills, skills_list):
    missing = list(set(skills_list) - set(found_skills))
    return missing