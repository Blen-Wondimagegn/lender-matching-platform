import { useState } from "react";
import LoanForm from "./components/LoanForm";
import Results from "./components/Results";
import "./App.css";

function App() {
  const [refreshKey, setRefreshKey] = useState(0);

  return (
    <main>
      <h1>Lender Matching Platform</h1>

      <LoanForm onComplete={() => setRefreshKey(refreshKey + 1)} />
      <Results key={refreshKey} />
    </main>
  );
}

export default App;