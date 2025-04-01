import cv2
import numpy as np

def draw_angle(image, angle, elbow):
    """Draw the calculated angle on the video frame."""
    cv2.putText(image, str(int(angle)), 
                tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

def draw_counter(image, counter, stage):
    """Display the rep counter and stage information on screen."""
    cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

    # Rep count
    cv2.putText(image, 'REPS', (15, 12), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image, str(counter), (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

    # Stage data
    cv2.putText(image, 'STAGE', (65, 12), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image, str(stage), (60, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
