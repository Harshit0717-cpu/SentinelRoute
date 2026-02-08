from ultralytics import YOLO
import cv2

class ObjectDetector:
    def __init__(self, model_path="yolov8n.pt"):
        print("Loading YOLO model...")
        self.model = YOLO(model_path)
        print("Model loaded.")

    def detect(self, frame):
        # Resize for CPU performance
        frame_resized = cv2.resize(frame, (640, 480))

        results = self.model(frame_resized, verbose=False)

        detections = []

        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                xyxy = box.xyxy[0].tolist()

                # Detect only PERSON class (class_id = 0 in COCO)
                if cls == 0 and conf > 0.5:
                    detections.append({
                        "class_id": cls,
                        "confidence": conf,
                        "bbox": xyxy
                    })

        return frame_resized, detections
