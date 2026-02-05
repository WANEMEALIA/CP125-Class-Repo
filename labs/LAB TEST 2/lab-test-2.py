#Programmer's name : Wany
#Program accepts 5 integer input values from the user and is stored in a list, print numbers in ascending order, calculate and find sum of all entered numbers and find and print the largest number
#Function to process numbers
def process_numbers():
    numbers = []

    # Input 5 integers
    for i in range(5):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    # Ascending order
    numbers.sort()
    print(f"Numbers in ascending order: {numbers}")

    # Sum of numbers
    total = sum(numbers)
    print(f"Sum of all numbers: {total}")

    # Largest number
    largest = max(numbers)
    print(f"Largest number: {largest}")

# Call the function
process_numbers()