import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 40, 48, 52, 60, 65, 72, 78, 85, 92]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(predictions)

new_data = pd.DataFrame({
    "Hours_Studied": [5, 7, 9]
})

new_predictions = model.predict(new_data)

print("\nNew Predictions:")
for hours, marks in zip(new_data["Hours_Studied"], new_predictions):
    print(f"{hours} hours -> {marks:.2f} marks")

print("\nCoefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
