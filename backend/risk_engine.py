from datetime import datetime

class RiskEngine:
    def __init__(self):
        self.event_weights = {
            "intrusion": 3
        }

    def calculate_risk(self, event_type, confidence):
        base_weight = self.event_weights.get(event_type, 1)
        risk_score = base_weight * confidence
        return round(risk_score, 2)

    def generate_event(self, event_type, track_id, confidence, camera_id=1):
        risk_score = self.calculate_risk(event_type, confidence)

        event = {
            "event_type": event_type,
            "track_id": track_id,
            "camera_id": camera_id,
            "confidence": round(confidence, 2),
            "risk_score": risk_score,
            "timestamp": datetime.now().isoformat()
        }

        return event
