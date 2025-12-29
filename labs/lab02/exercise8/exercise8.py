def calculate_bounce_height(current_height):
    """
    Calculate the next bounce height (80% of current).
    """
    return 0.8 * current_height


def is_ball_stopped(height):
    """
    Check if the ball has stopped (height < 1).
    """
    return height < 1


def calculate_bounce_count(initial_height):
    """
    Count how many times the ball bounces.
    """
    next_height = calculate_bounce_height(initial_height)
    
    if is_ball_stopped(next_height):
        return 0
    else:
        return 1 + calculate_bounce_count(next_height)


def calculate_total_distance(initial_height):
    """
    Calculate total distance traveled.
    """
    next_height = calculate_bounce_height(initial_height)

    if is_ball_stopped(next_height):
        return initial_height
    else:
        return initial_height + (calculate_bounce_count(initial_height) * 2)
    
height = 100
print("Bounce count:", calculate_bounce_count(height))
print("Total distance:", calculate_total_distance(height))