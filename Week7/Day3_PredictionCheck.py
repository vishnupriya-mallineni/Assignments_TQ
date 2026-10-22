import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Flatten, Dense
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

tf.keras.utils.set_random_seed(42)

model = Sequential([
    Input(shape=(28, 28)),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

probabilities = model.predict(X_test, verbose=0)
predictions = np.argmax(probabilities, axis=1)

correct_indices = np.where(predictions == y_test)[0]
incorrect_indices = np.where(predictions != y_test)[0]

print("Total Test Images:", len(y_test))
print("Correct Predictions:", len(correct_indices))
print("Incorrect Predictions:", len(incorrect_indices))
print("Accuracy:", round(accuracy_score(y_test, predictions), 4))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

plt.figure(figsize=(12, 5))

for i, index in enumerate(correct_indices[:10]):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_test[index], cmap="gray")
    plt.title(
        f"Actual: {y_test[index]}\nPredicted: {predictions[index]}",
        color="green"
    )
    plt.axis("off")

plt.suptitle("Correct Predictions")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 5))

for i, index in enumerate(incorrect_indices[:10]):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_test[index], cmap="gray")
    plt.title(
        f"Actual: {y_test[index]}\nPredicted: {predictions[index]}",
        color="red"
    )
    plt.axis("off")

plt.suptitle("Incorrect Predictions")
plt.tight_layout()
plt.show()

print("\nSample Incorrect Predictions:")

for index in incorrect_indices[:10]:
    print(
        f"Image {index}: "
        f"Actual = {y_test[index]}, "
        f"Predicted = {predictions[index]}, "
        f"Confidence = {probabilities[index, predictions[index]]:.3f}"
    )
