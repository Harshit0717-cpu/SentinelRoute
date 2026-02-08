from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "SentinelRoute Backend Live"}

@app.get("/api/test")
def test():
    return {"message": "Backend connection successful 🚀"}

@app.get("/api/detect")
def detect():
    return {
        "intrusion": False,
        "confidence": 0.12,
        "risk_score": 1.3
    }
