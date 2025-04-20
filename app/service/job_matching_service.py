# app/services/job_matcher.py

import psycopg2
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_db_connection():
    """Connect to the PostgreSQL database. Adjust parameters as needed."""
    conn = psycopg2.connect(
        host="postgres",         # if using docker-compose, service name might be 'postgres'
        database="resume_db",      # your actual database name
        user="postgres",
        password="postgrespw",
        port=5432
    )
    return conn

def fetch_all_jobs():
    """Fetch all jobs from the jobs table."""
    conn = get_db_connection()
    cur = conn.cursor()
    # Adjust the SQL query to match your actual jobs table columns
    cur.execute("SELECT job_id, title, description, experience_level, location FROM jobs;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def compute_resume_embedding(resume_data: dict) -> list:
    """
    Combine relevant resume fields into one string and compute its embedding.
    Converts every item to a string to avoid type errors.
    """
    fields = ["education", "workExperience", "skills", "certifications", "hobbies"]
    combined_text = " ".join(
        " ".join(str(item) for item in resume_data.get(field, []))
        for field in fields if resume_data.get(field)
    )
    embedding = model.encode([combined_text])
    return embedding

def compute_job_embeddings(jobs: list) -> list:
    """
    Given a list of job records, compute embeddings for each.
    We combine the job title and description for matching.
    """
    job_texts = []
    for job in jobs:
        job_id, title, description, exp_level, location = job
        combined_text = f"{title} {description}"
        job_texts.append(combined_text)
    job_embeddings = model.encode(job_texts)
    return job_embeddings

def match_jobs(resume_data: dict, top_n: int = 3) -> list:
    """
    Given extracted resume data (as a dict) and a number `top_n`, 
    returns the top matching jobs from the database.
    """
    resume_embedding = compute_resume_embedding(resume_data)
    jobs = fetch_all_jobs()
    if not jobs:
        return []

    job_embeddings = compute_job_embeddings(jobs)
    similarities = cosine_similarity(resume_embedding, job_embeddings)[0]

    job_matches = []
    for idx, score in enumerate(similarities):
        job_id, title, description, exp_level, location = jobs[idx]
        job_matches.append({
            "job_id": job_id,
            "title": title,
            "experience_level": exp_level,
            "location": location,
            "similarity": float(score)
        })

    job_matches.sort(key=lambda x: x["similarity"], reverse=True)
    return job_matches[:top_n]
