from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from datetime import datetime

app = FastAPI()

# ✅ CORS (Very Important for Vercel frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later we can restrict to your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Fake Event Generator (For Demo)
# -------------------------

events = []

def generate_fake_event():
    return {
        "event_type": "intrusion",
        "track_id": random.randint(1, 100),
        "camera_id": 1,
        "confidence": round(random.uniform(0.5, 0.9), 2),
        "risk_score": round(random.uniform(1.2, 2.8), 2),
        "timestamp": datetime.now().isoformat()
    }

# -------------------------
# Routes
# -------------------------

@app.get("/")
def root():
    return {"message": "SentinelRoute Backend is running 🚀"}

@app.get("/events")
def get_events():
    global events

    # Keep only last 10 events
    if len(events) > 10:
        events = events[-10:]

    # Add new event
    events.append(generate_fake_event())

    return {"events": events}


# -------------------------
# Required for Render
# -------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
