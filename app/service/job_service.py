from fastapi import FastAPI, HTTPException
import requests
import os

LINKEDIN_SCRAPER_API_KEY=os.getenv("LINKEDIN_SCRAPER_API_KEY", "dummy_key")

def scrape_jobs_list(field: str, page: str):
    response = requests.get(
        f"https://api.scrapingdog.com/linkedinjobs",
        params={"api_key": LINKEDIN_SCRAPER_API_KEY, "field": field, "page": page, "geoid": 102454443},
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Error fetching jobs: {response.text}")
    return response.json()

def scrape_job_detail(job_id):
    response = response = requests.get(
        f"https://api.scrapingdog.com/linkedinjobs",
        params={"api_key": LINKEDIN_SCRAPER_API_KEY, "job_id": {job_id}},
    )
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Error fetching jobs: {response.text}")
    return response.json()