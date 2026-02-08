import cv2
import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from detection import ObjectDetector
from tracking import SimpleTracker
from risk_engine import RiskEngine

app = FastAPI()

# ✅ Proper CORS for React dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

VIDEO_PATH = "../test_videos/test.mp4"

events_storage = []

def camera_loop():
    detector = ObjectDetector()
    tracker = SimpleTracker()
    risk_engine = RiskEngine()

    cap = cv2.VideoCapture(VIDEO_PATH)

    restricted_zone = (200, 150, 450, 400)
    inside_zone_ids = set()

    while True:
        ret, frame = cap.read()

        # 🔁 Loop video forever
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        frame_resized, detections = detector.detect(frame)
        detections = tracker.update(detections)

        current_inside_ids = set()

        for det in detections:
            x1, y1, x2, y2 = map(int, det["bbox"])
            confidence = det["confidence"]
            track_id = det["track_id"]

            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            intrusion = (
                restricted_zone[0] < center_x < restricted_zone[2]
                and restricted_zone[1] < center_y < restricted_zone[3]
            )

            if intrusion:
                current_inside_ids.add(track_id)

                if track_id not in inside_zone_ids:
                    event = risk_engine.generate_event(
                        event_type="intrusion",
                        track_id=track_id,
                        confidence=confidence
                    )

                    print("[EVENT GENERATED]:", event)

                    events_storage.append(event)

        inside_zone_ids = current_inside_ids


@app.get("/")
def root():
    return {"message": "SentinelRoute API Running"}


@app.get("/events")
def get_events():
    # Return only last 20 events
    return {"events": events_storage[-20:]}


# 🚀 Start camera processing in background thread
camera_thread = threading.Thread(target=camera_loop)
camera_thread.daemon = True
camera_thread.start()
