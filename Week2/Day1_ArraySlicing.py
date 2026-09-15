import numpy as np

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original Array:")
print(arr)

print("\nSingle Element:")
print(arr[0, 1])

print("\nFirst Row:")
print(arr[0])

print("\nSecond Row:")
print(arr[1])

print("\nFirst Column:")
print(arr[:, 0])

print("\nThird Column:")
print(arr[:, 2])

print("\nFirst Two Rows:")
print(arr[0:2])

print("\nFirst Two Columns:")
print(arr[:, 0:2])

print("\nSliced Array:")
print(arr[0:2, 1:3])
