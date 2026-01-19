import math
def calculate_mean(times):
    if len(times) == 0:
        return 0
    total = 0
    for i in times :
        total += i
    return total/len(times)

def stan_deviation(mean, times):
    if len(times) == 0:
        return 0
    variance_sum = 0
    for i in times:
        variance_sum += (i - mean) ** 2
        variance = variance_sum/len(times)
    return math.sqrt(variance)

def removing_slow_outliers(times, limit):
    cleaned = []
    for i in times:
        if i <= limit :
            cleaned.append(i)
    return cleaned

def filter_query_times(times):
    mean = calculate_mean(times)
    standard_deviation = stan_deviation(mean, times)
    limit = mean + standard_deviation 
    cleaned_times = removing_slow_outliers(times, limit)
    cleaned_times.sort()
    return cleaned_times


# Test
query_ = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_)
print(f"Filtered : {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]