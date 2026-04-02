#WANY
#Program checks and print the grade of one student

mark = float(input("Enter the student's mark : "))

def determine_grade(mark):
    if mark >= 80 :
        grade = "A"
    elif mark >= 60 :
        grade = "B"
    elif mark >= 40 :
        grade = "C"
    else :
        grade = "F"

    return grade

grade = determine_grade(mark)
print(f"Mark: {mark}, Grade: {grade}")






import csv

# Function 1
def read_bmi_file(file_name):

    f = open(file_name, "r", newline="")
    reader = csv.reader(f)

    next(reader)   # skip header

    total_height = 0
    count = 0

    print("BMI DATA:")

    for row in reader:
        print(row)

        height = float(row[1])
        total_height += height
        count += 1

    average = total_height / count
    print("Average Height:", average)

    f.close()


# Function 2
def add_new_data(file_name):

    gender = input("Enter gender: ")
    height = input("Enter height: ")
    weight = input("Enter weight: ")
    bmi = input("Enter BMI: ")

    f = open(file_name, "a", newline="")
    writer = csv.writer(f)

    writer.writerow([gender, height, weight, bmi])

    f.close()

    print("\nUpdated File Content:")

    f = open(file_name, "r", newline="")
    reader = csv.reader(f)

    for row in reader:
        print(row)

    f.close()


# Main Program
file_name = "bmi.csv"

read_bmi_file(file_name)
add_new_data(file_name)
