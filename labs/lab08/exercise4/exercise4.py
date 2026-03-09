# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:
import csv
def calculate_final_grades(input_file, output_file):
    f = open(input_file, "r")
    reader = csv.reader(f)
    next(reader)
    out = open(output_file, "w", newline= "")
    writer = csv.writer(out)

    writer.writerow(["student_id", "final_grade"])

    total = 0 
    count = 0

    for i in reader:
        student_id = i[0]
        midterm = float(i[1])
        final = float(i[2])
        final_grade = (midterm*0.4) + (final*0.6)
        writer.writerow([student_id, "{:.2f}".format(final_grade)])
        total += final_grade
        count += 1
    f.close()
    out.close()

    average = total /  count
    return average

# Test your code here
result = calculate_final_grades("data/scores.csv", "data/grades.csv")
print(f"Average final grade: {result:.2f}")
