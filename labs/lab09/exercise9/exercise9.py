import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def compare_subject_distributions(filename):
    df = pd.read_csv(filename)

    math_scores = df["Math"]
    science_scores = df["Science"]
    english_scores = df["English"]

    plt.hist(math_scores, bins=10, alpha=0.5, label="Math")
    plt.hist(science_scores, bins=10, alpha=0.5, label="Science")
    plt.hist(english_scores, bins=10, alpha=0.5, label="English")

    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.title("Score Distribution Comparison")

    plt.legend()

    plt.show()

    return len(df)


# Example usage

wany = compare_subject_distributions("labs/lab09/data/students.csv")
print("Number of students analyzed:", wany)