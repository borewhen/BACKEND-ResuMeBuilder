from fastapi import FastAPI, HTTPException
import requests
import os
from app.models.mock_interview import MockInterview
import openai
import re

LINKEDIN_SCRAPER_API_KEY=os.getenv("LINKEDIN_SCRAPER_API_KEY", "dummy_key")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY", "dummy_key")

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
        response = requests.get(
            f"https://api.scrapingdog.com/linkedinjobs",
            params={"api_key": LINKEDIN_SCRAPER_API_KEY, "job_id": {job_id}},
        )
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"Error fetching jobs: {response.text}")
        
        job_detail = response.json()
        return job_detail
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500)
    

def format_desc(job_id):
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
                    
                    1. Ensure it includes proper HTML tags (such as <h1>, <p>, <ul>, <li> where needed), and format them under one <div> with class name of job-desc-container. Don't include escaped newlines (\n) and backslashes (\\)
                    2. don't include description starting with headings such as "The Company" or "Description", just proceed with the content of the job description
                    3. don't use any of h1, h2, h3. All sections (eg. about us, responsibiltiies, requirements) must be <p> tag with bold style
                    """
                }
            ]
        )

        raw_html = completion["choices"][0]["message"]["content"].strip()
        formatted_html = re.sub(r"^```html\n|```$", "", raw_html).strip()
        print(f"formatted: {formatted_html}")
        return "".join(line.strip() for line in formatted_html.replace("\\n", "").replace('\\"', '"').split("\n"))
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500)



def get_company_name_and_job_position(job_id):
    """
    get company name and job position
    """
    if job_id == 42012811001:
        return {
            "company_name": "Nova AI",
            "job_position": "Full-Stack Developer"   
        }
    response = response = requests.get(
        f"https://api.scrapingdog.com/linkedinjobs",
        params={"api_key": LINKEDIN_SCRAPER_API_KEY, "job_id": {job_id}},
    )
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Error fetching jobs: {response.text}")
    
    job_data = response.json()[0]
    return {
        "company_name": job_data.get("company_name", "Unknown"),
        "job_position": job_data.get("job_position", "Unknown")
    }


def get_company_logo_from_job_id(job_id):
    """
    get company logo
    """
    response = response = requests.get(
        f"https://api.scrapingdog.com/linkedinjobs",
        params={"api_key": LINKEDIN_SCRAPER_API_KEY, "job_id": {job_id}},
    )
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Error fetching jobs: {response.text}")

    job_data = response.json()[0]
    response = requests.get(
        f"https://api.scrapingdog.com/linkedinjobs",
        params={"api_key": LINKEDIN_SCRAPER_API_KEY, "field": job_data.get("company_name", "Unknown"), "page": 1, "geoid": 102454443},
    )
    
    return response.json()[0].get("company_logo_url", "")