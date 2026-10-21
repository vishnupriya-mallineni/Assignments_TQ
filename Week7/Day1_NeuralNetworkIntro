import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = MLPClassifier(
    hidden_layer_sizes=(10,),
    activation="relu",
    solver="adam",
    max_iter=2000,
    random_state=42
)

model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)

print("Actual Values:")
print(y_test)

print("\nPredicted Values:")
print(predictions)

print("\nAccuracy:")
print(accuracy_score(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
))

experiments = []

for neurons in [5, 10, 20, 50]:
    experiment_model = MLPClassifier(
        hidden_layer_sizes=(neurons,),
        activation="relu",
        solver="adam",
        max_iter=2000,
        random_state=42
    )

    experiment_model.fit(X_train_scaled, y_train)

    experiment_predictions = experiment_model.predict(X_test_scaled)

    experiments.append({
        "Hidden_Neurons": neurons,
        "Accuracy": accuracy_score(y_test, experiment_predictions)
    })

results = pd.DataFrame(experiments)

print("\nMLP Experiment Results:")
print(results)

plt.figure(figsize=(8, 5))
plt.plot(model.loss_curve_)

plt.title("MLP Training Loss")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(
    results["Hidden_Neurons"],
    results["Accuracy"],
    marker="o"
)

plt.title("MLP Accuracy vs Hidden Neurons")
plt.xlabel("Number of Hidden Neurons")
plt.ylabel("Test Accuracy")
plt.xticks(results["Hidden_Neurons"])
plt.ylim(0, 1.05)
plt.grid(True)
plt.tight_layout()
plt.show()
