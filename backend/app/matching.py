from app.models import (
    Borrower,
    BusinessCredit,
    LoanRequest,
    LenderProgram
)



def evaluate_program(
        borrower,
        guarantor,
        business_credit,
        loan_request,
        program
):
    reasons = []
    eligible = True

    if guarantor.fico_score < program.min_fico:
        eligible = False
        reasons.append(
            f"FICO score {guarantor.fico_score} "
            f"is below minimum {program.min_fico}"
        )

    if business_credit.paynet_score < program.min_paynet:
        eligible = False
        reasons.append(
            f"PayNet score {business_credit.paynet_score} "
            f"is below minimum {program.min_paynet}"
        )

    if loan_request.amount < program.min_loan_amount:
        eligible = False
        reasons.append(
            f"Loan amount {loan_request.amount} "
            f"is below minimum {program.min_loan_amount}"
        )

    if loan_request.amount > program.max_loan_amount:
        eligible = False
        reasons.append(
            f"Loan amount {loan_request.amount} "
            f"exceeds maximum {program.max_loan_amount}"
        )

    if borrower.years_in_business < program.min_years_business:
        eligible = False
        reasons.append(
            f"Years in business {borrower.years_in_business} "
            f"is below minimum {program.min_years_business}"
        )
    current_year = 2025

    equipment_age = (
            current_year -
            loan_request.equipment_year
    )

    if (
            program.max_equipment_age is not None
            and
            equipment_age > program.max_equipment_age
    ):
        eligible = False

        reasons.append(
            f"Equipment age {equipment_age} "
            f"exceeds maximum "
            f"{program.max_equipment_age}"
        )
    fit_score = 100

    if guarantor.fico_score > program.min_fico:
        fit_score += 5

    if business_credit.paynet_score > program.min_paynet:
        fit_score += 5

    if borrower.years_in_business > program.min_years_business:
        fit_score += 5

    fit_score = min(fit_score, 100)

    if not eligible:
        fit_score = max(0, 100 - (len(reasons) * 25))

    return {
        "eligible": eligible,
        "fit_score": fit_score,
        "reasons": reasons
    }