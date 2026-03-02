# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    c = 0

    f = open(input_file, "r")
    lines = f.readlines()
    f.close()

    passing_students = []
    
    for i in lines:
        parts = i.split()
        student_id = parts[0]
        score = int(parts[1])
        
        if score >= 80:
            passing_students.append(student_id + " " + str(score) + "\n")
    
    
    # STEP 1 (again): OPEN output file (write mode)
    g = open(output_file, "w")
    
    # STEP 2b: WRITE passing students
    for record in passing_students:
        g.write(record)
    
    # STEP 4: CLOSE output file
    g.close()
    
    # Return number of passing students
    return len(passing_students)

# Test your code here
result = filter_passing_scores("data/scores.txt", "lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")
