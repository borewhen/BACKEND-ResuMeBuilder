## Backend Structure

```plaintext
backend/
├── app/
│   ├── __init__.py         # Initializes the app as a package
│   ├── main.py             # Entry point of the application
│   ├── database.py         # Database configuration and connection setup
│   ├── models.py           # Database models for ORM
│   ├── schemas.py          # Pydantic schemas for data validation
│   ├── routers/            # API route definitions
│   │   ├── __init__.py     # Initializes routers as a package
│   │   ├── user.py         # Routes related to user management
│   │   ├── job.py          # Routes related to job management
│   └── utils.py            # Utility functions and helpers
├── .env                    # Environment variables for the project
├── requirements.txt        # Python dependencies
├── Dockerfile              # Configuration for Docker containerization


How to run back-end
- open command prompt on the designated directory
- Open up environemnt : venv\Scripts\activate
- install dependencies: pip install -r requirements.txt
- set up enviornment variables to mysQl (.env file)
- initialise database:
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
- run the app : uvicorn app.main:app --reload

