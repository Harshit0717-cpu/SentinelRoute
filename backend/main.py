from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

app = FastAPI(title="SentinelRoute Backend")

# =========================
# CORS CONFIG
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For hackathon demo (safe enough)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# ROOT ROUTE (Health Check)
# =========================
@app.get("/")
def root():
    return {
        "status": "SentinelRoute Backend Live",
        "message": "AI Intrusion Detection API is running"
    }

# =========================
# SAMPLE TEST ROUTE
# =========================
@app.get("/api/test")
def test_api():
    return {
        "success": True,
        "data": "Backend connected successfully 🚀"
    }

# =========================
# Example Detection Route (Stub)
# =========================
@app.get("/api/detect")
def detect():
    # Replace this with your actual YOLO logic later
    return JSONResponse(
        content={
            "intrusion_detected": False,
            "risk_score": 0.12,
            "objects_detected": ["person"],
        }
    )
