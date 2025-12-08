# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    total_tent = math.ceil(participants / tent_capacity)
    total_cost = total_tent * tent_price
    total_meal_cost = meal_price * participants
    total = total_cost + total_meal_cost
    return total

# Test your code here
print("Testing Camping Logistics...")
