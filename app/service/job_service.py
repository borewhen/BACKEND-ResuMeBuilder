from fastapi import FastAPI, HTTPException
import requests
import os
from app.models.skills import Skill
import openai
import re

LINKEDIN_SCRAPER_API_KEY=os.getenv("LINKEDIN_SCRAPER_API_KEY", "dummy_key")


def scrape_jobs_list(field: str, page: str):
    """
    gets job list from scraping linkedin
    field (str): company / job name
    """
    response = requests.get(
        f"https://api.scrapingdog.com/linkedinjobs",
        params={"api_key": LINKEDIN_SCRAPER_API_KEY, "field": field, "page": page, "geoid": 102454443},
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Error fetching jobs: {response.text}")
    return response.json()


def scrape_job_detail(job_id):
    """
    gets job detail from scraping linkedin
    job_id (int): this is unique identifier for job
    """
    try:
        response = response = requests.get(
            f"https://api.scrapingdog.com/linkedinjobs",
            params={"api_key": LINKEDIN_SCRAPER_API_KEY, "job_id": {job_id}},
        )
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"Error fetching jobs: {response.text}")
        
        job_detail = response.json()
        completion = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Format the following job description as a valid HTML string that can be directly rendered on a webpage:
                    
                    ---
                    {job_detail[0].get("job_description", "No description available.")}
                    ---
                    
                    Ensure it includes proper HTML tags (such as <h1>, <p>, <ul>, <li> where needed), and format them under one <div> with class name of job-desc-container. Don't include escaped newlines (\n) and backslashes (\\)
                    """
                }
            ]
        )

        raw_html = completion["choices"][0]["message"]["content"].strip()
        formatted_html = re.sub(r"^```html\n|```$", "", raw_html).strip()
        job_detail[0]["job_description"] = "".join(line.strip() for line in formatted_html.replace("\\n", "").replace('\\"', '"').split("\n"))
        return job_detail
    except Exception as e:
        raise HTTPException(status_code=500)


def get_job_skills_required(db, job_id):
    """
    gets assosciated skills from the job
    job_id (int): this is unique identifier for job
    """
    skills = db.query(Skill).filter(job_id == job_id).all()
    if not skills: 
        return None
    return skills.__repr__()


def parse_skills_from_job(db, job_id):
    """
    parse job description and post this to DB
    job_description (str)
    """
    try:
        # check if job exist or not in db
        skills = db.query(Skill).filter(job_id == job_id).all()
        if not skills: 
            # fetch from scraping API 
            response = response = requests.get(
                f"https://api.scrapingdog.com/linkedinjobs",
                params={"api_key": LINKEDIN_SCRAPER_API_KEY, "job_id": {job_id}},
            )
            if response.status_code != 200:
                raise HTTPException(status_code=500, detail=f"Error fetching jobs: {response.text}")

            job_detail = response.json()

            # extract skills from job_desc
            completion = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                        Format the following job description. What are the technical skills and group them into related categories.
                        """
                    }
                ]
            )
        
        return skills.__repr__()
    except Exception:
        raise HTTPException(status_code=500)
    