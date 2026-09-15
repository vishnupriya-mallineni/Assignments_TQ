import numpy as np

data = np.array([10, 20, 30, 40, 50])

numpy_mean = np.mean(data)
numpy_median = np.median(data)
numpy_std = np.std(data)

manual_mean = sum(data) / len(data)

sorted_data = sorted(data)
middle = len(sorted_data) // 2
manual_median = sorted_data[middle]

variance = sum((x - manual_mean) ** 2 for x in data) / len(data)
manual_std = variance ** 0.5

print("Data:", data)

print("\nNumPy Calculations:")
print("Mean:", numpy_mean)
print("Median:", numpy_median)
print("Standard Deviation:", numpy_std)

print("\nManual Calculations:")
print("Mean:", manual_mean)
print("Median:", manual_median)
print("Standard Deviation:", manual_std)
