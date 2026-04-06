import pandas as pd

def critical_inventory(filename):
    df = pd.read_csv(filename)

    required_cols = {"ProductName", "CurrentStock", "ReorderThreshold", "LastRestockDays"}
        "critical_products": set(critical)

    return result

result = critical_inventory("labs/lab09/data/inventory.csv")
print(result)