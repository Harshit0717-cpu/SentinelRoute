import { useState } from "react";

const API_BASE = "https://sentinelroute-backend.onrender.com";

function App() {
  const [backendStatus, setBackendStatus] = useState("");
  const [detectionResult, setDetectionResult] = useState("");

  const checkBackend = async () => {
    try {
      const res = await fetch(`${API_BASE}/api/test`);
      const data = await res.json();
      setBackendStatus(data.data);
    } catch (err) {
      setBackendStatus("Backend not reachable ❌");
    }
  };

  const runDetection = async () => {
    try {
      const res = await fetch(`${API_BASE}/api/detect`);
      const data = await res.json();
      setDetectionResult(JSON.stringify(data, null, 2));
    } catch (err) {
      setDetectionResult("Detection failed ❌");
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>🚨 SentinelRoute Dashboard</h1>

      <button onClick={checkBackend} style={{ marginRight: "10px" }}>
        Test Backend Connection
      </button>

      <button onClick={runDetection}>
        Run Intrusion Detection
      </button>

      <div style={{ marginTop: "20px" }}>
        <h3>Backend Status:</h3>
        <p>{backendStatus}</p>
      </div>

      <div style={{ marginTop: "20px" }}>
        <h3>Detection Output:</h3>
        <pre>{detectionResult}</pre>
      </div>
    </div>
  );
}

export default App;
