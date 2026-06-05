# DECISIONS.md

## Lender Requirements Prioritized

I prioritized the lender criteria most commonly used for underwriting decisions:

* FICO Score
* PayNet Score
* Years in Business
* Loan Amount
* Equipment Age
* State Restrictions
* Industry Restrictions

These requirements provide meaningful lender matching and eligibility decisions.

## Simplifications Made

* Lender policies were manually entered from the provided PDFs instead of implementing automated PDF extraction.
* A simplified fit score model was used for ranking lenders.
* Hatchet workflow orchestration was not implemented due to time constraints.
* Authentication and user management were excluded to focus on core underwriting functionality.

## What I Would Add With More Time

* Automated PDF ingestion and rule extraction
* Hatchet workflow orchestration with parallel lender evaluation
* Advanced underwriting rules and weighted scoring
* Authentication and role-based access
* Enhanced React UI with policy management and reporting dashboards
