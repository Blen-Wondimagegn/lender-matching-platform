#Starts FastAPI and contains the API endpoints.

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal
from app.models import Base
from app import schemas, crud


#Create all tables defined in models.py if they don't already exist.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lender Matching Platform API")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Lender Matching API Running"}


@app.post("/borrowers")
def create_borrower(borrower: schemas.BorrowerCreate, db: Session = Depends(get_db)):
    return crud.create_borrower(db, borrower)


@app.post("/guarantors")
def create_guarantor(guarantor: schemas.GuarantorCreate, db: Session = Depends(get_db)):
    return crud.create_guarantor(db, guarantor)


@app.post("/business-credit")
def create_business_credit(credit: schemas.BusinessCreditCreate, db: Session = Depends(get_db)):
    return crud.create_business_credit(db, credit)


@app.post("/loan-requests")
def create_loan_request(loan: schemas.LoanRequestCreate, db: Session = Depends(get_db)):
    return crud.create_loan_request(db, loan)


@app.post("/lenders")
def create_lender(lender: schemas.LenderCreate, db: Session = Depends(get_db)):
    return crud.create_lender(db, lender)


@app.post("/lender-programs")
def create_lender_program(program: schemas.LenderProgramCreate, db: Session = Depends(get_db)):
    return crud.create_lender_program(db, program)


@app.post("/program-restrictions")
def create_program_restriction(
    restriction: schemas.ProgramRestrictionCreate,
    db: Session = Depends(get_db)
):
    return crud.create_program_restriction(db, restriction)


@app.get("/lenders")
def get_lenders(db: Session = Depends(get_db)):
    return crud.get_lenders(db)


@app.get("/lender-programs")
def get_lender_programs(db: Session = Depends(get_db)):
    return crud.get_lender_programs(db)


@app.get("/loan-requests")
def get_loan_requests(db: Session = Depends(get_db)):
    return crud.get_loan_requests(db)
