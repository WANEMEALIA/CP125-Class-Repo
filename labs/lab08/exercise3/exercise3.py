# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv
def calculate_order_total(products_file, order_file, output_file):
    prices = {}

    f = open(products_file, "r", newline="")
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        product_id = line[0]
        price = float(line[2])
        prices[product_id] = price
    f.close()

    grand_total = 0
    results = []

    f_order = open(order_file, "r", newline="")
    reader = csv.reader(f_order)
    next(reader)
    for line in reader:
        product_id = line[0]
        quantity = int(line[1])
        total_cost = prices[product_id] * quantity
        grand_total += total_cost
        results.append([product_id, total_cost])
    f_order.close()

    f_output = open(output_file, "w", newline="")
    writer = csv.writer(f_output)
    writer.writerow([product_id], [total_cost])

    for i in results:
        writer.writerow(i)
    f_output.close()

    return grand_total

# Test your code here
result = calculate_order_total("data/products.csv", "data/order.csv", "data/total.csv")
print(f"Grand total: ${result:.2f}")
