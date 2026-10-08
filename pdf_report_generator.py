from fpdf import FPDF


def generate_pdf_report(resume_name, ats_score, found_skills, missing_skills, recommendations, output_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="AI Resume Analyzer Report", ln=True, align="C")

    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Resume File Name: {resume_name}", ln=True)
    pdf.cell(200, 10, txt=f"ATS Score: {ats_score}%", ln=True)

    pdf.ln(8)

    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt="Skills Found:", ln=True)

    pdf.set_font("Arial", size=12)
    if found_skills:
        for skill in found_skills:
            pdf.cell(200, 8, txt=f"- {skill}", ln=True)
    else:
        pdf.cell(200, 8, txt="No skills detected.", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt="Missing Skills:", ln=True)

    pdf.set_font("Arial", size=12)
    if missing_skills:
        for skill in missing_skills:
            pdf.cell(200, 8, txt=f"- {skill}", ln=True)
    else:
        pdf.cell(200, 8, txt="No missing skills.", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt="Top Job Recommendations:", ln=True)

    pdf.set_font("Arial", size=12)
    if recommendations:
        for job in recommendations:
            pdf.cell(200, 8, txt=f"{job['job_title']} - Match: {job['match_percent']}%", ln=True)
    else:
        pdf.cell(200, 8, txt="No job recommendations.", ln=True)

    pdf.output(output_path)
    return output_path