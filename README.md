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
- Ensure you have access to the `.env` file. Refer to `env.template` for required variables.

---

## **Steps to Run the Back-End**

### **With Docker**

#### 1. **Setup pgAdmin**

To set up `pgAdmin`, run the following command to pull the `pgadmin4` image and launch a container:

```bash
docker run -p 5050:80 \
  -e 'PGADMIN_DEFAULT_EMAIL=pgadmin4@pgadmin.org' \
  -e 'PGADMIN_DEFAULT_PASSWORD=admin' \
  -d --name pgadmin4 dpage/pgadmin4
```

### 2. Configure env file
Create a .env file from the runtime.env.template, You will need to change the `DATABASE_URL to
postgresql://postgres:postgrespw@host.docker.internal/resume_db`

### 3. Launch Applications
Now do `docker compose up` to build the images. Now you should be able to visit http://localhost:8000/docs/

### 4. Setup DB Prerequisite
Log into PGADMIN http://localhost:5050/ with the password you set before. Enter the following configurations

##### For MacOs/Windows
Use `host.docker.internal` as Host name/address
![pgadmin](img/pgadmin.png)

Now create a new database in the server we created previously, and name it resume_db
![db](img/db.png)

#### Migration
create new migration file: 

`$ docker compose run migration revision -m "<your migration message here>"`

upgrade version of migration:

`$ docker compose run migration upgrade head`

downgrade version of migration:

`$ docker compose run migration downgrade -1`


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

### 3. Create Database
Open your local **pgAdmin** and create a new server with hostname ```localhost```, then fill up the username and password (if any).

Inside the server, create a database named ```resume_db```.

### 4. Fill the Environment Variables
Copy the environment template
```
cp .env.template .env
```
Fill up the ```DATABASE_URL``` field with your user
```
DATABASE_URL="postgresql://<your_username>:<your_password>"@localhost:5432/resume_db
```
or (if no password is set)
```
DATABASE_URL="postgresql://<your_username>@localhost:5432/resume_db
```

### 5. Migrations
Apply the migration to the database:

```bash
python -m alembic upgrade head
```

### 6. Run the Application
Start the FastAPI application with Uvicorn:
```bash
uvicorn app.main:app --reload
```

## Creating Python Virtual Environment (Venv)
NOTE: This is only useful if you are NOT using docker environment.

In this example we will use ```dip``` as the name to the virtual environment.

``` bash
python -m venv dip # or python3 -m venv dip
```
The python version of the venv will follow the head's version.

Upon succesfull creation, you must activate the environment to use i
```bash
source dip/bin/activate
```

Doing this correctly will change your command prompt to include ```(dip)``` in front of each line.