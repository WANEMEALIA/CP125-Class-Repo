import pandas as pd

def promotion_candidates(filename):
    df = pd.read_csv(filename)

    avg_performance = round(df["PerformanceScore"].mean(), 1)
    min_years_required = 2

    mask = (df["PerformanceScore"] > avg_performance) & (df["YearsOfService"] >= min_years_required)
    qualified = df[mask]["EmployeeName"]

    result = {
        "average_performance": avg_performance,
        "min_years_required": min_years_required,
        "candidate_count": len(qualified),
        "candidate_names": set(qualified)
    }

    return result

result = promotion_candidates("labs/lab09/data/employees.csv")
print(result)