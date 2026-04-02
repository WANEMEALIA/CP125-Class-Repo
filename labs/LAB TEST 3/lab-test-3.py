#importing csv file
import csv

#Function to calculate and print average height
def read_bmi(filename):
    f = open(filename, "r", newline ="")
    reader = csv.reader(f)
    next(reader)

    total_height = 0
    count = 0
    print("BMI data :")

    for i in reader:
        print(i)
        height = float(i[1])
        total_height += height
        count += 1
    
    average = total_height/count
    print(f"Average Height : {average}")
    f.close()

def adding_new_data(filename):
    gender = input("Enter gender: ")
    height = input("Enter height: ")
    weight = input("Enter weight: ")
    bmi = input("Enter BMI: ")

    f = open(filename, "a", newline="")
    writer = csv.writer(f)
    writer.writerow([gender, height, weight, bmi])
    f.close()

    print("\nUpdated File Content:")

    f = open(filename, "r", newline="")
    reader = reader.csv(f)
    for i in reader :
        print(i)

    f.close()

filename = "labs/LAB TEST 3/bmi.csv"
read_bmi(filename)
adding_new_data(filename)