def count_reps(angle, stage, counter):
    """
    Function to count reps based on the arm angle.
    """
    if angle > 160:
        stage = "down"
    if angle < 30 and stage == "down":
        stage = "up"
        counter += 1
        
    return stage, counter