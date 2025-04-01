import cv2
import mediapipe as mp
import numpy as np
import time
from src.utils.angle_calculations import calculate_angle
from src.utils.visualization import draw_angle, draw_counter

# Initialize Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height

# Rep counter variables
counter = 0
stage = None
exercise = "bicep_curl"  # Default exercise
start_time = time.time()
exercise_images = {
    "bicep_curl": "images/bicep_curl.jpg",
    "shoulder_press": "images/shoulder_press.jpg",
    "lateral_raise": "images/lateral_raise.jpg"
}

def load_exercise_image():
    if exercise in exercise_images:
        img = cv2.imread(exercise_images[exercise])
        if img is not None:
            return cv2.resize(img, (200, 200))  # Resize for overlay
    return None

def analyze_posture(angle):
    feedback = "Good Form"
    if exercise == "bicep_curl":
        if angle > 160:
            feedback = "Lower the arm"
        elif angle < 30:
            feedback = "Fully curl up"
    elif exercise == "shoulder_press":
        if angle > 160:
            feedback = "Lower arms fully"
        elif angle < 60:
            feedback = "Push up more"
    elif exercise == "lateral_raise":
        if angle < 30:
            feedback = "Raise arms higher"
        elif angle > 90:
            feedback = "Maintain shoulder level"
    return feedback

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    exercise_img = load_exercise_image()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        feedback = ""
        try:
            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark

                # Get mirrored coordinates
                shoulder = [1 - landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, 
                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [1 - landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, 
                         landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [1 - landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, 
                         landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                # Calculate angle
                angle = calculate_angle(shoulder, elbow, wrist)

                # Draw angle
                draw_angle(image, angle, elbow)

                # Analyze posture
                feedback = analyze_posture(angle)

                # Exercise counter logic
                if exercise == "bicep_curl":
                    if angle > 160:
                        stage = "down"
                    if angle < 30 and stage == "down":
                        stage = "up"
                        counter += 1

                elif exercise == "shoulder_press":
                    if angle > 160:
                        stage = "down"
                    if angle < 60 and stage == "down":
                        stage = "up"
                        counter += 1

                elif exercise == "lateral_raise":
                    if angle < 30:
                        stage = "down"
                    if angle > 90 and stage == "down":
                        stage = "up"
                        counter += 1

        except Exception as e:
            print(f"Error: {e}")

        # Draw counter UI
        elapsed_time = int(time.time() - start_time)
        cv2.putText(image, f"Time: {elapsed_time}s", (image.shape[1] - 150, image.shape[0] - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        draw_counter(image, counter, stage)

        # Overlay exercise image at the upper right corner
        if exercise_img is not None:
            x_offset = image.shape[1] - 210  # Adjust for right alignment
            y_offset = 10  # Upper right corner
            y_end, x_end = y_offset + exercise_img.shape[0], x_offset + exercise_img.shape[1]
            image[y_offset:y_end, x_offset:x_end] = exercise_img

        # Display exercise name at the lower left corner
        cv2.putText(image, exercise.replace('_', ' ').title(), (10, image.shape[0] - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Display posture feedback at the top center
        cv2.putText(image, feedback, (image.shape[1] // 2 - 100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if feedback == "Good Form" else (0, 0, 255),
                    2, cv2.LINE_AA)

        # Draw landmarks
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

        cv2.imshow('Mediapipe Feed', image)

        # Switch exercise every 30 seconds
        if elapsed_time > 30:
            exercise = list(exercise_images.keys())[(list(exercise_images.keys()).index(exercise) + 1) % len(exercise_images)]
            counter = 0
            stage = None
            start_time = time.time()
            exercise_img = load_exercise_image()

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()