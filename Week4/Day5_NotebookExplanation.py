# ============================================================
# CLASSIFICATION PROJECT: BREAST CANCER PREDICTION
# Goal: Predict whether a tumor is malignant or benign
# ============================================================


# ------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

# Pandas is used to organize the dataset into tables (DataFrames)
import pandas as pd

# Load a built-in classification dataset from scikit-learn
from sklearn.datasets import load_breast_cancer

# Used to split the dataset into training and testing sets
from sklearn.model_selection import train_test_split

# Used to standardize numerical features
from sklearn.preprocessing import StandardScaler

# Logistic Regression will be our classification algorithm
from sklearn.linear_model import LogisticRegression

# Metrics used to evaluate model performance
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ------------------------------------------------------------
# 2. DATA LOADING
# ------------------------------------------------------------

# Load the Breast Cancer Wisconsin dataset.
# The dataset contains numerical measurements of breast tumors.
data = load_breast_cancer()

# X contains the input features used to make predictions.
# Examples include radius, texture, perimeter, and area.
X = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

# y contains the target/output that we want to predict.
# 0 = malignant
# 1 = benign
y = pd.Series(
    data.target,
    name="target"
)

# Display basic information about the dataset
print("Dataset shape:", X.shape)

print("\nFirst 5 rows:")
print(X.head())

# Check how many examples belong to each target class
print("\nTarget distribution:")
print(y.value_counts())


# ------------------------------------------------------------
# 3. DATA PREPROCESSING
# ------------------------------------------------------------

# Check whether any input features contain missing values.
# Missing values may need to be filled or removed before training.
print("\nTotal missing values:")
print(X.isnull().sum().sum())


# Split the dataset into training and testing sets.
#
# Training data:
# Used by the model to learn patterns.
#
# Testing data:
# Kept separate and used to evaluate the trained model.
#
# test_size=0.20 means:
# 80% training data
# 20% testing data
#
# stratify=y maintains approximately the same class distribution
# in both the training and testing datasets.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])


# Standardize the numerical features.
#
# StandardScaler transforms features so they are approximately
# centered around 0 with a standard deviation of 1.
#
# This is useful because the dataset contains features with
# very different numerical scales.
scaler = StandardScaler()

# Learn the scaling parameters ONLY from the training data.
# Then transform the training data using those parameters.
X_train_scaled = scaler.fit_transform(X_train)

# Apply the SAME transformation to the test data.
#
# We do NOT fit the scaler again on test data because information
# from the test set should not influence model training.
X_test_scaled = scaler.transform(X_test)


# ------------------------------------------------------------
# 4. MODEL TRAINING
# ------------------------------------------------------------

# Create a Logistic Regression classification model.
#
# max_iter=1000 gives the algorithm enough iterations
# to converge while training.
model = LogisticRegression(max_iter=1000)

# Train the model using the scaled training features
# and their corresponding target labels.
#
# During training, the model learns relationships between
# tumor measurements and whether the tumor is malignant or benign.
model.fit(X_train_scaled, y_train)


# ------------------------------------------------------------
# 5. PREDICTION
# ------------------------------------------------------------

# Use the trained model to predict the classes
# for previously unseen test examples.
y_pred = model.predict(X_test_scaled)

# predict_proba() returns the model's estimated probability
# for each class instead of only returning 0 or 1.
y_probability = model.predict_proba(X_test_scaled)


# ------------------------------------------------------------
# 6. MODEL EVALUATION
# ------------------------------------------------------------

# Accuracy measures the percentage of test predictions
# that the model classified correctly.
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(round(accuracy, 4))


# The confusion matrix shows the number of correct
# and incorrect predictions for each class.
#
# It helps us understand:
# - Correct malignant predictions
# - Correct benign predictions
# - Malignant cases incorrectly classified as benign
# - Benign cases incorrectly classified as malignant
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# The classification report provides:
#
# Precision:
# How many predictions for a class were correct?
#
# Recall:
# How many actual examples of a class did the model identify?
#
# F1-score:
# A combined measure of precision and recall.
#
# Support:
# Number of actual examples belonging to each class.
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=data.target_names
    )
)


# ------------------------------------------------------------
# 7. REVIEW INDIVIDUAL PREDICTIONS
# ------------------------------------------------------------

# Create a DataFrame so we can easily compare:
# - Actual class
# - Predicted class
# - Probability of malignant
# - Probability of benign
results = pd.DataFrame({
    "Actual": y_test.reset_index(drop=True),
    "Predicted": y_pred,
    "Malignant_Probability": y_probability[:, 0],
    "Benign_Probability": y_probability[:, 1]
})

# Display the first 10 prediction results
print("\nSample Prediction Results:")
print(results.head(10))
