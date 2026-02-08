import numpy as np

class SimpleTracker:
    def __init__(self):
        self.next_id = 1
        self.tracks = {}

    def iou(self, boxA, boxB):
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])

        interArea = max(0, xB - xA) * max(0, yB - yA)

        boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
        boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

        iou = interArea / float(boxAArea + boxBArea - interArea + 1e-6)
        return iou

    def update(self, detections):
        updated_tracks = {}

        for det in detections:
            best_match_id = None
            best_iou = 0

            for track_id, track_box in self.tracks.items():
                score = self.iou(det["bbox"], track_box)
                if score > 0.3 and score > best_iou:
                    best_iou = score
                    best_match_id = track_id

            if best_match_id is not None:
                updated_tracks[best_match_id] = det["bbox"]
                det["track_id"] = best_match_id
            else:
                updated_tracks[self.next_id] = det["bbox"]
                det["track_id"] = self.next_id
                self.next_id += 1

        self.tracks = updated_tracks
        return detections
