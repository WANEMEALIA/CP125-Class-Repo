import math
def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """
    total = 0
    for i in times :
        total += i
    mean = total/len(times)

    variance_sum = 0
    for i in times :
        variance_sum += (i - mean) ** 2
    variance = variance_sum/len(times)

    stan_dev = math.sqrt(variance)

    limit = mean + stan_dev

    cleaned_times = []
    for i in times :
        if i <= limit :
            cleaned_times.append[i]

    cleaned_times.sort()
    return cleaned_times


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
