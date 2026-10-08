def generate_report(resume_name, ats_score, found_skills, missing_skills, recommendations):
    report = ""

    report += "=========================================\n"
    report += " AI RESUME ANALYZER REPORT\n"
    report += "=========================================\n\n"

    report += f"Resume File Name: {resume_name}\n\n"

    report += "---------- ATS SCORE ----------\n"
    report += f"ATS Score: {ats_score}%\n\n"

    report += "---------- SKILLS FOUND ----------\n"
    if found_skills:
        for skill in found_skills:
            report += f"- {skill}\n"
    else:
        report += "No skills detected.\n"
    report += "\n"

    report += "---------- MISSING SKILLS ----------\n"
    if missing_skills:
        for skill in missing_skills:
            report += f"- {skill}\n"
    else:
        report += "No missing skills.\n"
    report += "\n"

    report += "---------- JOB RECOMMENDATIONS ----------\n"
    if recommendations:
        for job in recommendations:
            report += f"{job['job_title']}  --> Match: {job['match_percent']}%\n"
    else:
        report += "No job recommendations.\n"

    report += "\n=========================================\n"
    report += " End of Report\n"
    report += "=========================================\n"

    return report