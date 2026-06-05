# Lender Matching Platform
## Overview

The Lender Matching Platform is a full-stack application that evaluates business loan applications against lender credit policies and identifies the best lender matches.

The system:

Stores lender policies in a normalized database structure
Evaluates loan applications against lender requirements
Generates eligibility decisions and rejection reasons
Calculates fit scores for ranking lenders
Persists underwriting results for reporting and auditing
Technology Stack
Backend
Python
FastAPI
SQLAlchemy
PostgreSQL
Frontend
React
TypeScript
Axios
Vite
Database
PostgreSQL
Local Development Setup
Prerequisites

Install:

Python 3.12+
Node.js 20+
PostgreSQL 16+
Git
Clone Repository
git clone <repository-url>
cd lender-matching-platform
Database Setup

## Create database:

CREATE DATABASE lender_matching_db;

Update database connection in:

backend/app/database.py

Example:

DATABASE_URL = "postgresql://postgres:password@localhost:5432/lender_matching_db"
Backend Setup

Navigate to backend:

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

## Architecture Overview
System Architecture
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

Represents database tables.

Examples:

Borrower
Guarantor
BusinessCredit
LoanRequest
Lender
LenderProgram
ProgramRestriction
MatchResult
Schemas Layer

Pydantic models used for:

Request validation
Response serialization
API contracts
CRUD Layer

Handles database operations:

Create
Read
Update
Delete

Keeps business logic separate from persistence.

Matching Engine

Evaluates loan applications against lender requirements.

Checks:

FICO score
PayNet score
Years in business
Loan amount
Equipment age
State restrictions
Industry restrictions
Equipment restrictions

Returns:

Eligibility status
Fit score
Rejection reasons
Database Design
Core Entities
Borrowers

Stores business information.

Guarantors

Stores personal guarantor credit information.

Business Credit

Stores commercial credit information.

Loan Requests

Stores equipment financing requests.

Lenders

Stores lender organizations.

Lender Programs

Stores lender-specific underwriting criteria.

Program Restrictions

Stores state, industry, and equipment exclusions.

Match Results

Stores underwriting outcomes.

API Documentation
Borrowers

Create borrower:

POST /borrowers

Get borrowers:

GET /borrowers
Guarantors

Create guarantor:

POST /guarantors
Business Credit

Create business credit:

POST /business-credit
Loan Requests

Create loan request:

POST /loan-requests

Get loan requests:

GET /loan-requests
Lenders

Create lender:

POST /lenders

Get lenders:

GET /lenders
Lender Programs

Create lender program:

POST /lender-programs

Get lender programs:

GET /lender-programs
Program Restrictions

Create restriction:

POST /program-restrictions
Underwriting

Run lender matching:

POST /underwrite/{loan_request_id}

Example:

POST /underwrite/1

Returns:

[
  {
    "program_id": 1,
    "program_name": "Apex A Program",
    "eligible": true,
    "fit_score": 100,
    "reasons": []
  }
]
Match Results

Retrieve underwriting history:

GET /match-results
Features Implemented
Lender policy management
Loan application management