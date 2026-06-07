## Lender Matching Platform
###  Overview

The Lender Matching Platform is a full-stack application that evaluates business loan applications against lender credit policies and identifies the best lender matches.

### The system:

* Stores lender policies in a normalized database structure
* Evaluates loan applications against lender requirements
* Generates eligibility decisions and rejection reasons
* Calculates fit scores for ranking lenders
* Persists underwriting results for reporting and auditing

### Technology Stack
* Backend 
* Python 
* FastAPI 
* SQLAlchemy 
* PostgreSQL 
* Frontend 
* React 
* TypeScript 
* Axios 
* Vite

### Local Development Setup

### Install:
* Python 3.12+
* Node.js 20+
* PostgreSQL 16+

### Git
#### Clone Repository

git clone https://github.com/Blen-Wondimagegn/lender-matching-platform

cd lender-matching-platform



# Database Setup
### Create database:

CREATE DATABASE lender_matching_db;

Update database connection in:

backend/app/database.py

Example:

DATABASE_URL = "postgresql://postgres:password@localhost:5432/lender_matching_db"
Backend Setup

### Navigate to backend:

cd backend

Create virtual environment:

python -m venv 

### Activate:

Git Bash
source venv/Scripts/activate
Windows CMD
venv\Scripts\activate

### Install dependencies:

* pip install fastapi 
* pip install uvicorn 
* pip install sqlalchemy 
* pip install psycopg2-binary

### Start backend:
python -m uvicorn app.main:app --reload
Swagger UI:
http://127.0.0.1:8000/docs


### Frontend Setup
Navigate to frontend:
cd frontend

### Install dependencies:

* npm install
* npm install axios

### Start React application:

* npm run dev

Frontend URL:
 http://localhost:5173



## Architecture Overview
### System Architecture

React + TypeScript

        |
        v
     Axios
        |
        v
     FastAPI
        |
        v
 Matching Engine

        |
        v

PostgreSQL

Backend Layers

Models Layer


