# Function 1: Display file content and calculate average height
def section1():
    f = open("data.csv", "r")

    lines = f.readlines()
    print("File Content:")

    total = 0
    count = 0

    for i in range(len(lines)):
        print(lines[i].strip())

        if i > 0:   # skip header
            data = lines[i].strip().split(",")
            height = float(data[1])
            total = total + height
            count = count + 1

    average = total / count
    print("Average Height:", average)

    f.close()


# Function 2: Add new data and print updated file
def section2():
    gender = input("Enter Gender: ")
    height = input("Enter Height: ")
    weight = input("Enter Weight: ")
    bmi = input("Enter BMI Index: ")

    f = open("data.csv", "a")
    f.write("\n" + gender + "," + height + "," + weight + "," + bmi)
    f.close()

    print("\nUpdated File Content:")

    f = open("data.csv", "r")
    print(f.read())
    f.close()


# Main program
section1()
section2()