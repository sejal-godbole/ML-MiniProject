# Human Landmark Detection for Gym Pose Estimation

## Project Overview
This project focuses on real-time gym pose estimation using **MediaPipe Pose** and **OpenCV**, enabling accurate exercise form tracking and repetition counting. It helps users maintain correct posture, track progress, and prevent injuries by providing real-time feedback based on detected key points.

## Key Features
- **Pose Detection:** Uses **MediaPipe Pose** to detect 33 key points on the human body.
- **Exercise Classification:** Identifies different exercises based on joint angles.
- **Repetition Counter:** Tracks and counts reps dynamically for exercises like **bicep curls, shoulder press, and lateral raises**.
- **Real-Time Processing:** Supports **live video analysis** via webcam.
- **Performance Metrics:** Evaluates form accuracy using joint angles and movement patterns.

## Model Architecture
The system utilizes:
- **MediaPipe Pose:** Detects **33 landmarks** on the human body (shoulders, elbows, wrists, hips, knees, ankles, etc.).
- **Angle Calculation:** Computes joint angles to determine movement patterns.
- **Repetition Counting:** Uses a state machine approach to detect complete reps (e.g., **up → down → up** for a valid rep).

## Preprocessing
- **Frame Processing:** Converts video frames from BGR to RGB for better detection.
- **Key Point Extraction:** Extracts relevant joint coordinates for pose analysis.
- **Angle Computation:** Calculates angles to classify movement stages.

## Exercise Classifier and Rep Counter
The rep counter is implemented using a simple state transition model:
- **"Up" Position:** Start of the movement (e.g., arm extended in bicep curl).
- **"Down" Position:** End of the movement (e.g., arm bent in bicep curl).
- **Valid Rep:** When the model detects an "up → down → up" transition.

## Example Exercises
| Exercise           | Key Angle for Detection |
|--------------------|-------------------------|
| **Bicep Curl**     | Elbow Angle             |
| **Shoulder Press** | Shoulder & Elbow Angles |
| **Lateral Raise**  | Shoulder Angle          |

## Results
- **Accuracy:** The pose estimation achieves **high precision** in detecting key points.
- **Repetition Counting:** Provides **real-time tracking** with minimal error.

## Future Scope
- **Adding More Exercises:** Extend to squats, push-ups, lunges, and deadlifts.
- **Voice Feedback:** Real-time alerts like *"Straighten your back!"*.
- **Mobile App Integration:** Deploying on Android/iOS for gym users.
- **AI-Based Form Correction:** Suggesting posture improvements using deep learning models.

## Conclusion
This project demonstrates **real-time gym pose estimation and repetition counting**, providing users with a **smart fitness tracking** solution. By leveraging **pose detection and joint angle analysis**, the system enhances workout quality and reduces injury risk. Future advancements will focus on Smartwatch & Fitness Band Integration: Tracking movements with wearables for better accuracy and More Exercise Support: Expanding the system to cover more workout types.
