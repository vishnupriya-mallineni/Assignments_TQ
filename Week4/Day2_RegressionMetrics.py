import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

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

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

print("Actual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(predictions)

print("\nMean Absolute Error:", mae)
print("Mean Squared Error:", mse)
