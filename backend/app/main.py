#Starts FastAPI and contains the API endpoints.

from fastapi import FastAPI

from app.database import engine
from app.models import Base

app = FastAPI()
#Create all tables defined in models.py if they don't already exist.
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Lender Matching API Running"}