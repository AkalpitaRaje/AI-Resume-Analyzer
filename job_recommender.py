from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_jobs_ai(resume_text, jobs_data, top_n=5):
    """
    AI Based Job Recommendation using TF-IDF and Cosine Similarity
    """

    job_texts = []
    job_titles = []

    for job in jobs_data:
        job_titles.append(job["job_title"])

        combined_text = str(job["skills"]) + " " + str(job["description"])
        job_texts.append(combined_text)

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer(stop_words="english")
    job_vectors = vectorizer.fit_transform(job_texts)
    resume_vector = vectorizer.transform([resume_text])

    # Cosine similarity
    similarity_scores = cosine_similarity(resume_vector, job_vectors)[0]

    recommendations = []
    for i in range(len(job_titles)):
        recommendations.append({
            "job_title": job_titles[i],
            "match_percent": round(similarity_scores[i] * 100, 2)
        })

    # Sort by highest match
    recommendations = sorted(recommendations, key=lambda x: x["match_percent"], reverse=True)

    return recommendations[:top_n]