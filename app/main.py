from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.routers import user, job, video  # Import routers

app = FastAPI()

# Include the routers for user job and video routes
app.include_router(user.router, prefix="/user", tags=["Users"])
app.include_router(job.router, prefix="/job", tags=["Jobs"])
app.include_router(video.router, prefix="/video", tags=["VideoUpload"])

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