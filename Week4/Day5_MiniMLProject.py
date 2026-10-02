# 1. Import libraries
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# 2. Load the dataset
data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")

print("Dataset shape:", X.shape)
print("\nFirst 5 rows:")
print(X.head())

print("\nTarget distribution:")
print(y.value_counts())

# 3. Check for missing values
print("\nMissing values:", X.isnull().sum().sum())

# 4. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# 5. Scale the features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Create the model
model = LogisticRegression(max_iter=1000)

# 7. Train the model
model.fit(X_train_scaled, y_train)

# 8. Make predictions
y_pred = model.predict(X_test_scaled)

# 9. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy, 4))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=data.target_names
))

# 10. View prediction probabilities
probabilities = model.predict_proba(X_test_scaled)

results = pd.DataFrame({
    "Actual": y_test.reset_index(drop=True),
    "Predicted": y_pred,
    "Malignant_Probability": probabilities[:, 0],
    "Benign_Probability": probabilities[:, 1]
})

print("\nPrediction Results:")
print(results.head(10))
