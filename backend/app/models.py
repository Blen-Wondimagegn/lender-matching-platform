#Defines database tables like Borrower, Loan Application, Lender Policy, and Match Result.
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from app.database import Base

#Create tables in the lender_matching_db database
class Borrower(Base):
    __tablename__ = "borrowers"

    id = Column(Integer, primary_key=True, index=True)

    business_name = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    state = Column(String, nullable=False)

    years_in_business = Column(Integer, nullable=False)
    annual_revenue = Column(Integer, nullable=False)

    is_startup = Column(Boolean, default=False)


class Guarantor(Base):
    __tablename__ = "guarantors"

    id = Column(Integer, primary_key=True, index=True)

    borrower_id = Column(
        Integer,
        ForeignKey("borrowers.id")
    )

    fico_score = Column(Integer)
    bankruptcy_flag = Column(Boolean, default=False)


class BusinessCredit(Base):
    __tablename__ = "business_credit"

    id = Column(Integer, primary_key=True, index=True)

    borrower_id = Column(
        Integer,
        ForeignKey("borrowers.id")
    )

    paynet_score = Column(Integer)
    trade_lines = Column(Integer)


class LoanRequest(Base):
    __tablename__ = "loan_requests"

    id = Column(Integer, primary_key=True, index=True)

    borrower_id = Column(
        Integer,
        ForeignKey("borrowers.id")
    )

    amount = Column(Integer)
    term_months = Column(Integer)

    equipment_type = Column(String)
    equipment_year = Column(Integer)
class Lender(Base):
    __tablename__ = "lenders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class LenderProgram(Base):
    __tablename__ = "lender_programs"

    id = Column(Integer, primary_key=True, index=True)

    lender_id = Column(Integer, ForeignKey("lenders.id"))

    name = Column(String, nullable=False)

    min_fico = Column(Integer)
    min_paynet = Column(Integer)
    min_years_business = Column(Integer)

    min_loan_amount = Column(Integer)
    max_loan_amount = Column(Integer)

    max_term_months = Column(Integer)
    max_equipment_age = Column(Integer)


class ProgramRestriction(Base):
    __tablename__ = "program_restrictions"

    id = Column(Integer, primary_key=True, index=True)

    program_id = Column(Integer, ForeignKey("lender_programs.id"))

    restriction_type = Column(String, nullable=False)
    value = Column(String, nullable=False)


class MatchResult(Base):
    __tablename__ = "match_results"

    id = Column(Integer, primary_key=True, index=True)

    loan_request_id = Column(Integer, ForeignKey("loan_requests.id"))
    program_id = Column(Integer, ForeignKey("lender_programs.id"))

    eligible = Column(Boolean, default=False)
    fit_score = Column(Integer, default=0)
    rejection_reason = Column(String)
