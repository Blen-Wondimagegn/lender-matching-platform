#Contains database functions like create, read, update, delete(database actions)

from sqlalchemy.orm import Session
from app import models, schemas


def create_borrower(db: Session, borrower: schemas.BorrowerCreate):
    db_borrower = models.Borrower(**borrower.model_dump())
    db.add(db_borrower)
    db.commit()
    db.refresh(db_borrower)
    return db_borrower


def create_guarantor(db: Session, guarantor: schemas.GuarantorCreate):
    db_guarantor = models.Guarantor(**guarantor.model_dump())
    db.add(db_guarantor)
    db.commit()
    db.refresh(db_guarantor)
    return db_guarantor


def create_business_credit(db: Session, credit: schemas.BusinessCreditCreate):
    db_credit = models.BusinessCredit(**credit.model_dump())
    db.add(db_credit)
    db.commit()
    db.refresh(db_credit)
    return db_credit


def create_loan_request(db: Session, loan: schemas.LoanRequestCreate):
    db_loan = models.LoanRequest(**loan.model_dump())
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def create_lender(db: Session, lender: schemas.LenderCreate):
    db_lender = models.Lender(**lender.model_dump())
    db.add(db_lender)
    db.commit()
    db.refresh(db_lender)
    return db_lender


def create_lender_program(db: Session, program: schemas.LenderProgramCreate):
    db_program = models.LenderProgram(**program.model_dump())
    db.add(db_program)
    db.commit()
    db.refresh(db_program)
    return db_program


def create_program_restriction(db: Session, restriction: schemas.ProgramRestrictionCreate):
    db_restriction = models.ProgramRestriction(**restriction.model_dump())
    db.add(db_restriction)
    db.commit()
    db.refresh(db_restriction)
    return db_restriction


def get_lenders(db: Session):
    return db.query(models.Lender).all()


def get_lender_programs(db: Session):
    return db.query(models.LenderProgram).all()


def get_loan_requests(db: Session):
    return db.query(models.LoanRequest).all()
def get_loan_requests(db: Session):
    return db.query(models.LoanRequest).all()


def get_loan_request_by_id(db: Session, loan_request_id: int):
    return db.query(models.LoanRequest).filter(
        models.LoanRequest.id == loan_request_id
    ).first()


def get_borrower_by_id(db: Session, borrower_id: int):
    return db.query(models.Borrower).filter(
        models.Borrower.id == borrower_id
    ).first()


def get_business_credit_by_borrower_id(db: Session, borrower_id: int):
    return db.query(models.BusinessCredit).filter(
        models.BusinessCredit.borrower_id == borrower_id
    ).first()


def get_all_lender_programs(db: Session):
    return db.query(models.LenderProgram).all()


def get_guarantor_by_borrower_id(db: Session, borrower_id: int):
    return db.query(models.Guarantor).filter(
        models.Guarantor.borrower_id == borrower_id
    ).first()
def get_restrictions_by_program_id(db: Session, program_id: int):
    return db.query(models.ProgramRestriction).filter(
        models.ProgramRestriction.program_id == program_id
    ).all()
def get_match_results(db: Session):
    return db.query(models.MatchResult).all()

def create_match_result(
    db: Session,
    loan_request_id: int,
    program_id: int,
    eligible: bool,
    fit_score: int,
    rejection_reason: str
):
    db_result = models.MatchResult(
        loan_request_id=loan_request_id,
        program_id=program_id,
        eligible=eligible,
        fit_score=fit_score,
        rejection_reason=rejection_reason
    )

    db.add(db_result)
    db.commit()
    db.refresh(db_result)

    return db_result
