
def was_backward_detected(waypoints):
    for i in range(1, len(waypoints)):
        previous = waypoints[i - 1]
        current = waypoints[i]
        
        # Tuple unpacking
        x1, y1, z1 = previous
        x, y, z = current
        
        # Check for backward movement
        if x < x1 or y < y1:
            return True
    return False

    """
    Return True if drone moved backward in x or y, False otherwise.
    Use tuple unpacking.
    """

# Test
path = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True
