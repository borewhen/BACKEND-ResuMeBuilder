# Back-End Folder Structure

```plaintext
app/
├── routers/                # API route definitions
│   ├── __init__.py
│   ├── auth.py
│   └── user.py
├── services/               # Utilities and business logic for route handlers
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

## With Docker

### 1. Setup PGADMIN
In short, the command above pulls the pgadmin4 image from docker and run it in a container with port number 5050
docker run -p 5050:80 -e 'PGADMIN_DEFAULT_EMAIL=pgadmin4@pgadmin.org' -e 'PGADMIN_DEFAULT_PASSWORD=admin' -d --name pgadmin4 dpage/pgadmin4

### 2. Configure env file
Create a .env file from the runtime.env.template, You will need to change the DATABASE_URL to
postgresql://postgres:postgrespw@host.docker.internal/resume_db

### 3. Launch Applications
Now do docker compose up to build the images. Now you should be able to visit http://localhost:8000/docs/

### 4. Setup DB Prerequisite
Log into PGADMIN http://localhost:5050/ with the password you set before. Enter the following configurations

##### For MacOs/Windows
Use `host.docker.internal` as Host name/address
![pgadmin](img/pgadmin.png)

Now create a new database in the server we created previously, and name it resume_db
![db](img/db.png)

#### Migrating the database
make the initiate migration for the DB with the following commands: 

`$ docker compose run migration`


### 2. 

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