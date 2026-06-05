# Database Setup

Create database:

CREATE DATABASE lender_matching_db;

Update database connection in:

backend/app/database.py

Example:

DATABASE_URL = "postgresql://postgres:password@localhost:5432/lender_matching_db"
Backend Setup

# Navigate to backend:

cd backend

Create virtual environment:

python -m venv venv

Activate:

Git Bash
source venv/Scripts/activate
Windows CMD
venv\Scripts\activate

Install dependencies:

pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install psycopg2-binary

Start backend:

python -m uvicorn app.main:app --reload

Swagger UI:

http://127.0.0.1:8000/docs
Frontend Setup

Navigate to frontend:

cd frontend

Install dependencies:

npm install
npm install axios

Start React application:

npm run dev

Frontend URL:

http://localhost:5173
Architecture Overview# lender-matching-platform