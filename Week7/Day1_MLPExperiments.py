import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

epochs = [100, 500, 1000]
hidden_layers = [(5,), (10,), (20,), (10, 10)]

results = []

plt.figure(figsize=(10, 6))

for layers in hidden_layers:
    for epoch in epochs:
        model = MLPClassifier(
            hidden_layer_sizes=layers,
            activation="relu",
            solver="adam",
            max_iter=epoch,
            random_state=42
        )

        model.fit(X_train, y_train)

        train_predictions = model.predict(X_train)
        test_predictions = model.predict(X_test)

        train_accuracy = accuracy_score(
            y_train, train_predictions
        )

        test_accuracy = accuracy_score(
            y_test, test_predictions
        )

        results.append({
            "Hidden_Layers": str(layers),
            "Max_Iterations": epoch,
            "Actual_Iterations": model.n_iter_,
            "Train_Accuracy": train_accuracy,
            "Test_Accuracy": test_accuracy,
            "Final_Loss": model.loss_
        })

        print(f"\nHidden Layers: {layers}")
        print(f"Max Iterations: {epoch}")
        print(f"Actual Iterations: {model.n_iter_}")
        print(f"Training Accuracy: {train_accuracy:.3f}")
        print(f"Testing Accuracy: {test_accuracy:.3f}")
        print(f"Final Loss: {model.loss_:.4f}")

        plt.plot(
            model.loss_curve_,
            label=f"Layers={layers}, Max Iter={epoch}"
        )

results_df = pd.DataFrame(results)

print("\nMLP Experiment Comparison:")
print(results_df.round(3).to_string(index=False))

plt.title("MLP Training Loss Comparison")
plt.xlabel("Training Iterations")
plt.ylabel("Loss")
plt.legend(fontsize=8)
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))

for layers in hidden_layers:
    subset = results_df[
        results_df["Hidden_Layers"] == str(layers)
    ]

    plt.plot(
        subset["Max_Iterations"],
        subset["Test_Accuracy"],
        marker="o",
        label=f"Layers {layers}"
    )

plt.title("MLP Accuracy Comparison")
plt.xlabel("Maximum Training Iterations")
plt.ylabel("Testing Accuracy")
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

results_df.to_csv("mlp_experiment_results.csv", index=False)
