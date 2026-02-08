import { useEffect, useState } from "react";

function App() {
  const [events, setEvents] = useState([]);

  const fetchEvents = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/events");
      const data = await response.json();
      setEvents(data.events.reverse());
    } catch (error) {
      console.error("Error fetching events:", error);
    }
  };

  useEffect(() => {
    fetchEvents();
    const interval = setInterval(fetchEvents, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>🚨 SentinelRoute Dashboard</h1>
      <h3>Live Intrusion Alerts</h3>

      {events.length === 0 ? (
        <p>No events detected.</p>
      ) : (
        events.map((event, index) => {
          const highRisk = event.risk_score > 2;

          return (
            <div
              key={index}
              style={{
                border: highRisk ? "2px solid red" : "1px solid #ff9999",
                padding: "12px",
                marginBottom: "12px",
                borderRadius: "8px",
                backgroundColor: highRisk ? "#ffcccc" : "#ffe6e6",
                boxShadow: highRisk
                  ? "0 0 10px rgba(255,0,0,0.6)"
                  : "none",
              }}
            >
              <strong>Track ID:</strong> {event.track_id} <br />
              <strong>Risk Score:</strong> {event.risk_score} <br />
              <strong>Confidence:</strong> {event.confidence} <br />
              <strong>Time:</strong> {event.timestamp}
            </div>
          );
        })
      )}
    </div>
  );
}

export default App;
