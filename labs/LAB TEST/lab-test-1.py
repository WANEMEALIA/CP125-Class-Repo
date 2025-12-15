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