def count_shoulder_press(angle, stage, counter):
    """
    Counts shoulder press repetitions based on elbow angle.

    Parameters:
    - angle: The detected elbow angle.
    - stage: Current movement stage ("down" or "up").
    - counter: Current rep count.

    Returns:
    - Updated stage and counter.
    """
    if angle > 170:  # Arms fully extended (press completed)
        stage = "up"
    elif angle < 90 and stage == "up":  # Arms bent (press reset)
        stage = "down"
        counter += 1  # Count rep

    return stage, counter