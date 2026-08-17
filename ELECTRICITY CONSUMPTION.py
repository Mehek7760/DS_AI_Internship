import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("ELECTRICITY CONSUMPTION.csv")

# Features
X = data[
    ["Temperature", "Appliances", "TimeOfDay", "PreviousUsage"]
]

# Target
y = data["CurrentUsage"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Check model performance
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# Enter new household details
print("\nEnter New Household Details")

temperature = float(input("Temperature: "))
appliances = int(input("Number of appliances: "))
time = int(input("Time of day (0-23): "))
previous_usage = float(input("Previous electricity usage: "))

# Create DataFrame with correct feature names
new_data = pd.DataFrame([[
    temperature,
    appliances,
    time,
    previous_usage
]], columns=[
    "Temperature",
    "Appliances",
    "TimeOfDay",
    "PreviousUsage"
])

# Predict electricity consumption
prediction = model.predict(new_data)

print("\nPredicted Electricity Consumption:",
      round(prediction[0], 2), "kWh")