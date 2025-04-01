import cv2
import mediapipe as mp
import numpy as np
from src.utils import draw_landmarks
from src.pose_estimation import PoseEstimator

def main():
    cap = cv2.VideoCapture(0)  # Open webcam
    pose = PoseEstimator()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)  # Flip horizontally for a mirror effect
        results = pose.process(frame)
        
        if results.pose_landmarks:
            draw_landmarks(frame, results)
        
        cv2.imshow('Live Pose Estimation', frame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
