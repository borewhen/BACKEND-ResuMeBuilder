from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user, job,resume_extraction, mock_interview , course # Import routers

app = FastAPI(debug=True)

# Include the routers for user and job routes
app.include_router(user.router, prefix="/user", tags=["Users"])
app.include_router(job.router, prefix="/job", tags=["Jobs"])
app.include_router(resume_extraction.router, prefix="/resume", tags=["resume_extraction"])
app.include_router(mock_interview.router, prefix="/mock_interview", tags=["mock_interview"])
app.include_router(course.router, prefix="/course", tags=["course"])

# Define allowed origins
origins = [
    "http://localhost:3000", # development environment
    # Add the production URL here
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handler for unexpected exceptions
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "An unexpected error occurred. Please try again later.",
            "type": "InternalServerError",
        },
    )