import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(arr)
print("Shape:", arr.shape)

reshaped = arr.reshape(2, 3)

print("\nReshaped Array:")
print(reshaped)
print("Shape:", reshaped.shape)

flattened = reshaped.flatten()

print("\nFlattened Array:")
print(flattened)
print("Shape:", flattened.shape)
