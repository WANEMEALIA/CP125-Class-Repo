import pandas as pd
import csv

def compare_averages(filename):
    totals = {"Math": 0, "Science": 0, "English": 0}
    count = 0
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            totals["Math"] += float(row["Math"])
            totals["Science"] += float(row["Science"])
            totals["English"] += float(row["English"])
            count += 1
    averages = {subject: round(totals[subject] / count, 1) for subject in totals}

    best_subject = max(averages, key=averages.get)
    worst_subject = min(averages, key=averages.get)

    averages["best_subject"] = best_subject
    averages["worst_subject"] = worst_subject

    return averages

