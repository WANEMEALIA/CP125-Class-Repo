def process_student():
    # Responsibility 1: Getting input
    name = input("Enter student name: ")
    score = int(input("Enter score: "))
    
    # Responsibility 2: Making decision
    if score >= 50:
        status = "Pass"
    else:
        status = "Fail"
    
    # Responsibility 3: Displaying output
    print(f"Student: {name}")
    print(f"Score: {score}")
    print(f"Status: {status}")

# Run the function
process_student()