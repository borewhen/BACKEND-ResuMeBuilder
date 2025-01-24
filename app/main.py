from fastapi import FastAPI
from app.routers import user, job  # Import routers

app = FastAPI()

# Include the routers for user and job routes
app.include_router(user.router, prefix="/user", tags=["Users"])
app.include_router(job.router, prefix="/job", tags=["Jobs"])

# Example of a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Portal API"}
