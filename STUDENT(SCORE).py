import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = pd.read_csv("STUDENT(SCORE).csv")

# Input features
X = data[[
    "StudyHours",
    "Attendance",
    "PreviousMarks",
    "AssignmentMarks",
    "InternalMarks"
]]

# Target
y = data["Result"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create classification model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy * 100, "%")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Take new student details
print("\nEnter New Student Details")

study_hours = float(input("Study Hours: "))
attendance = float(input("Attendance Percentage: "))
previous_marks = float(input("Previous Marks: "))
assignment_marks = float(input("Assignment Marks: "))
internal_marks = float(input("Internal Marks: "))

# Create input for prediction
new_student = [[
    study_hours,
    attendance,
    previous_marks,
    assignment_marks,
    internal_marks
]]

# Prediction
prediction = model.predict(new_student)

print("\nPredicted Result:", prediction[0])