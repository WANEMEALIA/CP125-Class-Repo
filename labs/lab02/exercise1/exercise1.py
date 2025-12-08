# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:
    
def is_budget_sufficient(length, km_per_liter, price_per_liter, budget):
    total_length = length * 2
    litre = total_length / km_per_liter
    total_cost = litre * price_per_liter
    if total_cost <= budget:
        return True
    else: 
        return False

# Test your code here
print("Testing Road Trip Budgeter...")