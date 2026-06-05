#Defines request/response shapes for the API.
#what data the frontend/API will send and return.
from pydantic import BaseModel
from typing import Optional


class BorrowerCreate(BaseModel):
    business_name: str
    industry: str
    state: str
    years_in_business: int
    annual_revenue: int
    is_startup: bool = False


class GuarantorCreate(BaseModel):
    borrower_id: int
    fico_score: int
    bankruptcy_flag: bool = False


class BusinessCreditCreate(BaseModel):
    borrower_id: int
    paynet_score: int
    trade_lines: int


class LoanRequestCreate(BaseModel):
    borrower_id: int
    amount: int
    term_months: int
    equipment_type: str
    equipment_year: int


class LenderCreate(BaseModel):
    name: str


class LenderProgramCreate(BaseModel):
    lender_id: int
    name: str
    min_fico: Optional[int] = None
    min_paynet: Optional[int] = None
    min_years_business: Optional[int] = None
    min_loan_amount: Optional[int] = None
    max_loan_amount: Optional[int] = None
    max_term_months: Optional[int] = None
    max_equipment_age: Optional[int] = None


class ProgramRestrictionCreate(BaseModel):
    program_id: int
    restriction_type: str
    value: str