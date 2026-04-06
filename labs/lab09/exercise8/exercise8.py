import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def plot_subject_maximums(filename):
    df = pd.read_csv(filename)

    subjects = ["Math", "Science", "English", "Physics", "Chemistry"]

    max_scores = [df[sub].max() for sub in subjects]

    plt.plot(subjects, max_scores, marker='o', color='blue')

    plt.xlabel("Subject")
    plt.ylabel("Maximum Score")
    plt.title("Maximum Scores by Subject")
    plt.show()

    return len(df)

df = plot_subject_maximums("labs/lab09/data/students.csv")
print("Number of students analyzed:", df)
