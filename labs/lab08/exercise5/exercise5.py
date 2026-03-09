# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv
def summarize_sales(input_file, output_file):
    f = open(input_file, "r")
    reader = csv.reader(f)
    next(reader)

    revenues = []

    for i in reader :
        quantity = int(i[1])
        price = float(i[2])

        revenue = quantity * price
        revenues.append(revenue)
    f.close()

    total = sum(revenues)
    average = total/len(revenues)
    highest = max(revenues)
    lowest = min(revenues)
    out = open(output_file, "w")

    out.write(f"Total Revenue : ${total:.2f} \n")
    out.write(f"Average Revenue : ${average:.2f} \n")
    out.write(f"Highest Revenue : ${highest:.2f} \n")
    out.write(f"Lowest Revenue : ${lowest:.2f} \n")

    out.close()
    return (total, average, highest, lowest)
# Test your code here
result = summarize_sales("labs/labs08/exercise5/data/sales.csv", "labs/labs08/exercise5/data/summary.txt")
print(result)
