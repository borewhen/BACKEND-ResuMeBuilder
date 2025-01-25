# Back-End Folder Structure

```plaintext
app/
├── routers/                # API route definitions
│   ├── __init__.py
│   ├── auth.py
│   └── user.py
├── services/               # Utilities and business logic
│   ├── __init__.py
│   └── user_service.py
├── schemas/                # Pydantic schemas for data validation
│   ├── __init__.py
│   └── user.py
├── models/                 # Database models for ORM
│   ├── __init__.py
│   └── user.py
├── database.py 
├── __init__.py
├── main.py
```

# Back-End Setup Instructions

Follow the steps below to set up and run the back-end application:

---

## **Prerequisites**

- A virtual environment (`venv`) set up for the project
- Ensure you have access to the `.env` variable, refer to env.template for what variables you need

---

## **Steps to Run the Back-End**


## Without Docker
### 1. Activate the Virtual Environment
Activate the virtual environment for the project:

- Windows: 
```bash
venv\Scripts\activate
```
- Mac/Linux: 
```bash
source .venv/bin/activate
```
### 2. Install Dependencies
Install all required dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 3. Migrations
Apply the migration to the database:

```bash
alembic upgrade head
```

### 4. Run the Application
Start the FastAPI application with Uvicorn:
```bash
uvicorn app.main:app --reload
```