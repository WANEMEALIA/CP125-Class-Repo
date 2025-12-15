# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour):
    if vehicle_type.lower() == "electric":
        return 2.00

    elif vehicle_type.lower() == "hybrid":
        if hour >= 22 or hour <= 6:
            return 2.00
        else:
            return 5.00

    else:
        return 5.00


print("Testing Dynamic Parking Rate...")
