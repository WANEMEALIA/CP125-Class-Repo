# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    if vehicle_type == "Electric":
        rate = 2
        total_fee = rate
    elif vehicle_type == "Hybrid":
        if hour_24 >= 22 and hour_24 <= 6:
            rate = 2
        else :
            rate = 5
    else: 
        rate = 5
# Test your code here
print("Testing Dynamic Parking Rate...")
