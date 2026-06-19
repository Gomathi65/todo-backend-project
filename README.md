# todo-backend-project



# Todo Backend Project

## Setup

### Create Virtual Environment

python -m venv venv

### Activate

venv\Scripts\activate

### Install Packages

pip install -r backend/requirements.txt

### Run Application

uvicorn app.main:app --reload

## API Endpoints

POST /todos

GET /todos

PUT /todos/{id}

DELETE /todos/{id}

## Docker

docker build -t todo-api .

docker run -p 8000:8000 todo-api