## Lender Matching Platform
Overview

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

Create database:

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
Architecture Overview
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
Matching engine
Eligibility evaluation
Rejection reasoning
Fit score calculation
State restrictions
Equipment age validation
PostgreSQL persistence
React frontend
FastAPI REST API
Future Improvements
Automated PDF lender guideline ingestion
OCR and document parsing
Hatchet workflow orchestration
Parallel underwriting evaluation
Advanced fit score algorithms
Authentication and authorization
Policy versioning
Dashboard and analytics
File upload interface for lender PDFs
DECISIONS.md documenting:
Which lender requirements you prioritized
Simplifications made and why
What you would add with more time

Add this as your DECISIONS.md.

DECISIONS.md
Overview

This document outlines the key design decisions made during development of the Lender Matching Platform, including lender requirement prioritization, simplifications, and future improvements.

Lender Requirements Prioritized

The lender guidelines contained a large number of underwriting rules. Due to the project timeline, I prioritized requirements that have the highest impact on lender eligibility decisions and demonstrate the core matching workflow.

The following requirements were implemented:

Credit Requirements
Minimum FICO Score
Minimum PayNet Score
Bankruptcy Flag
Business Requirements
Years in Business
Startup Identification
Annual Revenue
Loan Requirements
Minimum Loan Amount
Maximum Loan Amount
Loan Term
Equipment Requirements
Equipment Type
Equipment Age
Geographic Restrictions
State-based exclusions
Industry Restrictions
Industry-based exclusions
Matching Outputs
Eligibility Decision
Rejection Reasons
Fit Score Ranking

These criteria represent the majority of lender screening logic and provide meaningful lender recommendations.

Policy Modeling Decisions

A normalized database structure was chosen to make lender policies extensible and maintainable.

Lenders

Stores lender information.

Lender Programs

Stores lender-specific underwriting programs and thresholds.

Program Restrictions

Stores exclusions such as:

Restricted States
Restricted Industries
Restricted Equipment Types

This design allows new lenders and programs to be added without modifying application code.

Simplifications Made
PDF Parsing

The assignment mentions receiving lender guidelines in PDF format.

For this implementation, lender policies were manually entered into the database after reviewing the PDF documents.

Reason:

Focus was placed on policy modeling and matching logic.
Manual ingestion demonstrates the normalized design without introducing PDF extraction complexity.
The database structure supports future automated PDF ingestion.
Fit Score Calculation

The fit score uses a simplified scoring model based on:

FICO Score
PayNet Score
Years in Business
Eligibility Criteria

Reason:

Provides lender ranking functionality.
Keeps underwriting logic understandable and easy to extend.

Future versions could use weighted scoring models.

Workflow Orchestration

Hatchet workflow orchestration was not implemented in the current version.

Reason:

The matching process executes quickly with the current dataset.
Time was prioritized toward lender policy modeling, API development, and UI implementation.

Future versions would use Hatchet for:

Parallel lender evaluation
Retry handling
Background processing
Workflow monitoring
Authentication

Authentication and authorization were not implemented.

Reason:

Focus was placed on underwriting functionality.
Authentication is orthogonal to the core matching engine.

Future versions could use JWT-based authentication.

Future Improvements

Given additional development time, the following enhancements would be implemented.

Automated PDF Ingestion

Create a lender onboarding workflow that:

Upload PDF
      ↓
Extract Policy Data
      ↓
Normalize Rules
      ↓
Save to Database

Potential tools:

PyPDF2
pdfplumber
OCR processing
LLM-assisted extraction
Advanced Underwriting Rules

Support additional lender criteria such as:

Debt Service Coverage Ratio (DSCR)
Revenue thresholds
Trade line requirements
Industry-specific rules
Equipment valuation logic
Advanced Fit Scoring

Replace the current scoring model with weighted scoring.

Example:

FICO Score           30%
PayNet Score         25%
Years in Business    20%
Revenue              15%
Equipment Profile    10%

This would produce more realistic lender rankings.

Hatchet Workflow Integration

Use Hatchet to:

Run lender evaluations in parallel
Retry failed evaluations
Track workflow execution status
Improve scalability
Enhanced Frontend

Additional UI features:

Dynamic application forms
Lender policy management dashboard
Match result filtering
Detailed lender comparison view
PDF upload interface
Reporting and Analytics

Provide dashboards showing:

Approval rates
Most matched lenders
Common rejection reasons
Application volume trends
Final Decision Summary

The primary focus of this implementation was:

Building a normalized and extensible lender policy model.
Implementing a functional underwriting and matching engine.
Providing clear eligibility and rejection reasoning.
Persisting underwriting results for future retrieval.
Delivering a complete FastAPI, PostgreSQL, React, and TypeScript solution.

The resulting system demonstrates the core architecture required to support additional lenders, underwriting rules, and automated policy ingestion in future iterations.

keep it vey short
DECISIONS.md
Lender Requirements Prioritized

I prioritized the lender criteria most commonly used for underwriting decisions:

FICO Score
PayNet Score
Years in Business
Loan Amount
Equipment Age
State Restrictions
Industry Restrictions

These requirements provide meaningful lender matching and eligibility decisions.

Simplifications Made
Lender policies were manually entered from the provided PDFs instead of implementing automated PDF extraction.
A simplified fit score model was used for ranking lenders.
Hatchet workflow orchestration was not implemented due to time constraints.
Authentication and user management were excluded to focus on core underwriting functionality.
What I Would Add With More Time
Automated PDF ingestion and rule extraction
Hatchet workflow orchestration with parallel lender evaluation
Advanced underwriting rules and weighted scoring
Authentication and role-based access
Enhanced React UI with policy management and reporting dashboards

This version is short, professional, and appropriate for a take-home assignment.

give a steps to add to read me how to  clone form github

Add this section to your README.md.

Clone and Run the Project
1. Clone the Repository
git clone https://github.com/<your-username>/lender-matching-platform.git
cd lender-matching-platform
2. Backend Setup

Navigate to the backend folder:

cd backend

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

Git Bash

source venv/Scripts/activate

Windows Command Prompt

venv\Scripts\activate

Install dependencies:

pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv

Start the backend:

python -m uvicorn app.main:app --reload

Swagger API documentation:

http://127.0.0.1:8000/docs
3. Database Setup

Create PostgreSQL database:

CREATE DATABASE lender_matching_db;

Update the database connection string in:

backend/app/database.py
4. Frontend Setup

Open a new terminal and navigate to the frontend folder:

cd frontend

Install dependencies:

npm install
npm install axios

Start the React application:

npm run dev

Open:

http://localhost:5173
5. Run the Application

Make sure all three components are running:

PostgreSQL
FastAPI Backend (http://127.0.0.1:8000)
React Frontend (http://localhost:5173)

The application is now ready to use.