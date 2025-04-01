import numpy as np

def calculate_angle(a, b, c):
    """
    Calculate the angle between three points.
    :param a: First point (shoulder)
    :param b: Second point (elbow)
    :param c: Third point (wrist)
    :return: Angle in degrees
    """
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360.0 - angle

    return angle


