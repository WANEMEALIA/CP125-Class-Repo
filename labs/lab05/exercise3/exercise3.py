
def find_bottleneck_index(traceroute):
    """
    Find the index of the hop where the largest latency jump begins.
    """
    max_jump = 0
    bottleneck_index = 0
    for i in range (len(traceroute) - 1):
        current_latency = traceroute[i][1]
        next_latency = traceroute[i+1][1]
        jump = abs(next_latency - current_latency)
        if jump > max_jump:
            max_jump = jump
            bottleneck_index = i

    return bottleneck_index
# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
