from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.routers import user, job  # Import routers

app = FastAPI()

# Include the routers for user and job routes
app.include_router(user.router, prefix="/user", tags=["Users"])
app.include_router(job.router, prefix="/job", tags=["Jobs"])

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