import { useEffect, useState } from "react";
import { api } from "../api";

type MatchResult = {
  id: number;
  loan_request_id: number;
  program_id: number;
  eligible: boolean;
  fit_score: number;
  rejection_reason: string;
};

export default function Results() {
  const [results, setResults] = useState<MatchResult[]>([]);
  const [loading, setLoading] = useState(false);

  const loadResults = async () => {
    try {
      setLoading(true);

      const response = await api.get("/match-results");

      setResults(response.data);
    } catch (error) {
      console.error("Failed to load results", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    void loadResults();
  }, []);

  return (
    <section className="card">
      <h2>Match Results</h2>

      <button onClick={loadResults}>
        Refresh Results
      </button>

      {loading && <p>Loading...</p>}

      {!loading && results.length === 0 && (
        <p>No match results found.</p>
      )}

      {results.map((result) => (
        <div key={result.id} className="result">
          <h3>Program #{result.program_id}</h3>

          <p>
            <strong>Status:</strong>{" "}
            {result.eligible ? "Eligible" : "Not Eligible"}
          </p>

          <p>
            <strong>Fit Score:</strong>{" "}
            {result.fit_score}/100
          </p>

          <p>
            <strong>Reason:</strong>{" "}
            {result.rejection_reason || "All criteria met"}
          </p>
        </div>
      ))}
    </section>
  );
}