import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("Training Images Shape:", X_train.shape)
print("Training Labels Shape:", y_train.shape)

print("\nTesting Images Shape:", X_test.shape)
print("Testing Labels Shape:", y_test.shape)

print("\nImage Dimensions:", X_train[0].shape)
print("Pixel Data Type:", X_train.dtype)

print("\nFirst Image Label:", y_train[0])
print("\nFirst Image Pixel Values:")
print(X_train[0])

print("\nMinimum Pixel Value:", X_train.min())
print("Maximum Pixel Value:", X_train.max())

print("\nUnique Labels:")
print(np.unique(y_train))

labels, counts = np.unique(y_train, return_counts=True)

print("\nNumber of Training Images Per Digit:")
for label, count in zip(labels, counts):
    print(f"Digit {label}: {count} images")

plt.figure(figsize=(10, 5))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_train[i], cmap="gray")
    plt.title(f"Label: {y_train[i]}")
    plt.axis("off")

plt.suptitle("MNIST Handwritten Digit Samples")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(labels, counts)

plt.title("MNIST Training Label Distribution")
plt.xlabel("Digit")
plt.ylabel("Number of Images")
plt.xticks(labels)
plt.grid(axis="y")
plt.tight_layout()
plt.show()
