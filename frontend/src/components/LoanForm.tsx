import { useState } from "react";
import { api } from "../api";

export default function LoanForm({ onComplete }: { onComplete: () => void }) {
  const [loanId, setLoanId] = useState<number | null>(null);
  const [status, setStatus] = useState("");

  async function createApplication() {
    setStatus("Creating application...");

    const borrower = await api.post("/borrowers", {
      business_name: "ABC Trucking",
      industry: "Transportation",
      state: "NV",
      years_in_business: 5,
      annual_revenue: 750000,
      is_startup: false,
    });

    const borrowerId = borrower.data.id;

    await api.post("/guarantors", {
      borrower_id: borrowerId,
      fico_score: 720,
      bankruptcy_flag: false,
    });

    await api.post("/business-credit", {
      borrower_id: borrowerId,
      paynet_score: 700,
      trade_lines: 5,
    });

    const loan = await api.post("/loan-requests", {
      borrower_id: borrowerId,
      amount: 50000,
      term_months: 48,
      equipment_type: "Semi Truck",
      equipment_year: 2022,
    });

    setLoanId(loan.data.id);
    setStatus(`Application created. Loan ID: ${loan.data.id}`);
  }

  async function runUnderwriting() {
    if (!loanId) return;

    setStatus("Running underwriting...");
    await api.post(`/underwrite/${loanId}`);
    setStatus("Underwriting complete.");
    onComplete();
  }

  return (
    <section className="card">
      <h2>Loan Application</h2>
      <p>Create a sample application and run lender matching.</p>

      <button onClick={createApplication}>Create Sample Application</button>
      <button onClick={runUnderwriting} disabled={!loanId}>
        Run Underwriting
      </button>

      <p>{status}</p>
    </section>
  );
}