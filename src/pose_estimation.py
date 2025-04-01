import mediapipe as mp
import cv2

class PoseEstimator:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    def process(self, image):
        if image is None:
            raise ValueError("Image not found. Please check the path.")

        # Convert BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process with MediaPipe Pose
        results = self.pose.process(image_rgb)

        return results

    def draw_landmarks(self, image, results):
        mp_drawing = mp.solutions.drawing_utils
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
            
    
