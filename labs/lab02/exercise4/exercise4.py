# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def calculate_hourly_rate(vehicle_type, hour):
    # Electric vehicles
    if vehicle_type.lower() == "electric":
        return 2.0

    # Hybrid vehicles
    elif vehicle_type.lower() == "hybrid":
        if hour >= 22 or hour < 6:
            return 2.0
        else:
            return 5.0

    # All other vehicles
    else:
        return 5.0

print("Testing Dynamic Parking Rate...")
