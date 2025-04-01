def count_lateral_raise(angle, stage, counter):
    """
    Counts lateral raise repetitions based on shoulder angle.

    Parameters:
    - angle: The detected shoulder angle.
    - stage: Current movement stage ("down" or "up").
    - counter: Current rep count.

    Returns:
    - Updated stage and counter.
    """
    if angle > 90:  # Arm raised (rep completed)
        stage = "up"
    elif angle < 20 and stage == "up":  # Arm lowered (reset for next rep)
        stage = "down"
        counter += 1  # Count rep

    return stage, counter