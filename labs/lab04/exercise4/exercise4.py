
def analyze_performance(lap_times):
    n = len(lap_times)

    first_half_size = (n + 1) // 2

    # Calculate first half average
    total_first = 0
    for i in range(first_half_size):
        total_first = total_first + lap_times[i]
    first_avg = total_first / first_half_size

    # Calculate second half average
    total_second = 0
    for i in range(first_half_size, n):
        total_second = total_second + lap_times[i]
    second_avg = total_second / (n - first_half_size)

    # Athlete faded if second half average is worse (higher)
    if second_avg > first_avg:
        return True
    else:
        return False



# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
