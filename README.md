# SentinelRoute – AI Intrusion Detection System

SentinelRoute is a real-time AI-powered surveillance system that detects intrusions in restricted zones and shows live alerts on a dashboard.

Built for IIT Roorkee Hackathon 2026.

---

## What It Does

- Detects people using YOLOv8
- Tracks individuals across frames
- Detects intrusion in restricted area
- Calculates risk score
- Sends events through FastAPI backend
- Displays live alerts on React dashboard

---

## Tech Stack

- Python
- YOLOv8
- OpenCV
- FastAPI
- React (Vite)

---

##  How To Run

Backend:
cd backend
python -m uvicorn main:app --reload

Frontend:
cd frontend
npm install
npm run dev

Open:
http://localhost:5173

---

##  Author

Harshit Dubey
