#Starts FastAPI and contains the API endpoints.

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal
from app.models import Base
from app import schemas, crud
from app.matching import evaluate_program


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

@app.post("/underwrite/{loan_request_id}")
def run_underwriting(
    loan_request_id: int,
    db: Session = Depends(get_db)
):
    loan_request = crud.get_loan_request_by_id(
        db,
        loan_request_id
    )

    borrower = crud.get_borrower_by_id(
        db,
        loan_request.borrower_id
    )

    guarantor = crud.get_guarantor_by_borrower_id(
        db,
        borrower.id
    )

    business_credit = crud.get_business_credit_by_borrower_id(
        db,
        borrower.id
    )

    programs = crud.get_all_lender_programs(db)

    results = []

    for program in programs:
        restrictions = crud.get_restrictions_by_program_id(
            db,
            program.id
        )

        result = evaluate_program(
            borrower,
            guarantor,
            business_credit,
            loan_request,
            program,
            restrictions
        )

        results.append({
            "program_id": program.id,
            "program_name": program.name,
            "eligible": result["eligible"],
            "fit_score": result["fit_score"],
            "reasons": result["reasons"]
        })

    results.sort(
        key=lambda x: x["fit_score"],
        reverse=True
    )

    return results