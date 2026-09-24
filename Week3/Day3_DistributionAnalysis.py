import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Age": [22, 24, 25, 27, 28, 30, 32, 35, 40, 55],
    "Salary": [35000, 38000, 40000, 42000, 45000, 48000, 50000, 55000, 60000, 120000]
}

df = pd.DataFrame(data)

for column in ["Age", "Salary"]:
    mean = df[column].mean()
    median = df[column].median()

    print(column)
    print("Mean:", mean)
    print("Median:", median)

    if mean > median:
        print("Distribution may be right-skewed")
    elif mean < median:
        print("Distribution may be left-skewed")
    else:
        print("Distribution may be symmetric")

    plt.figure(figsize=(8, 5))
    plt.hist(df[column], bins=5, edgecolor="black")
    plt.axvline(mean, linestyle="--", label="Mean")
    plt.axvline(median, linestyle=":", label="Median")
    plt.title(f"{column} Distribution")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
