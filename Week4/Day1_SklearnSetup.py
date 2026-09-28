import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

data = {
    "Hours_Studied": [2, 3, 4, 5, 6, 7, 8, 9, 4, 6],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95, 72, 88],
    "Final_Marks": [52, 58, 63, 68, 74, 79, 84, 90, 65, 81]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Attendance"]]
y = df["Final_Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(predictions)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

print("\nMean Absolute Error:", mae)
print("Mean Squared Error:", mse)
