# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient():
    length = int(input("Enter length of the trip: "))
    km_per_liter = float(input("Enter fuel used: "))
    price_per_liter = float(input("Enter cost of fuel per litre: "))
    budget = float(input("Enter budget RM: "))
    total_length = length * 2
    litre = total_length / km_per_liter
    total_cost = litre * price_per_liter
    return total_cost

def determine_status(total_cost, budget):
    if total_cost >= budget:
        print("Money is not enough for a round trip.")
    else: 
        print("Money is enough for a round trip.")
    pass

# Test your code here
print("Testing Road Trip Budgeter...")
status = determine_status(total_cost, budget)