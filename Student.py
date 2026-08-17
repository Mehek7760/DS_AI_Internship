import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("student.csv")

# Input features
X = data[["StudyHours", "Attendance"]]

# Target/output
y = data["Result"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the model
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Take input from user
study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))

# Predict result
prediction = model.predict([[study_hours, attendance]])

print("Predicted Result:", prediction[0])