import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = pd.read_csv("LOAN APPROVAL.csv")

# Features
X = data[
    ["Income", "Age", "CreditScore", "LoanAmount", "EmploymentYears"]
]

# Target
y = data["LoanStatus"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
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

# New applicant details
print("\nEnter New Applicant Details")

income = float(input("Income: "))
age = int(input("Age: "))
credit_score = int(input("Credit Score: "))
loan_amount = float(input("Loan Amount: "))
employment_years = int(input("Employment Years: "))

# Prediction
new_applicant = [[
    income,
    age,
    credit_score,
    loan_amount,
    employment_years
]]

prediction = model.predict(new_applicant)

print("\nLoan Status:", prediction[0])