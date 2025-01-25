## Backend Structure

```plaintext
app/
├── routers/                # API route definition
│   ├── __init__.py
│   ├── auth.py
│   └── user.py
├── services/               # package for utilities / service function, holding business logic
│   ├── __init__.py 
│   └── user_service.py
├── schemas/                # Pydantic schemas for data validation
│   ├── __init__.py
│   └── user.py
├── models/                 # Database models for ORM
│   ├── __init__.py
│   └── user.py
├── database.py             # Database configuration and connection setup
└── utils/
    ├── __init__.py
    └── auth.py
├── .env                    # Environment variables for the project
├── .env.templat            # Env template
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

