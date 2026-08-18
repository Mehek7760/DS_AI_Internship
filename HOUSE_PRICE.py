import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# --------------------------------
# Load CSV dataset
# --------------------------------

df = pd.read_csv("HOUSE_PRICE.csv")

print("Dataset:")
print(df)

# --------------------------------
# SUPERVISED LEARNING
# Regression
# --------------------------------

# Input features
X = df[["Area", "Bedrooms", "Bathrooms", "Age"]]

# Target variable
y = df["Price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("\nActual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(y_pred)

# Model evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Absolute Error:", mae)
print("R2 Score:", r2)

# --------------------------------
# Predict price of a new house
# --------------------------------

new_house = [[1600, 3, 2, 5]]

predicted_price = model.predict(new_house)

print(
    "\nPredicted price of new house:",
    round(predicted_price[0], 2),
    "lakhs"
)

# --------------------------------
# UNSUPERVISED LEARNING
# K-Means Clustering
# --------------------------------

cluster_data = df[["Area", "Bedrooms", "Bathrooms", "Age"]]

# Standardize data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(cluster_data)

# Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Assign clusters
df["Cluster"] = kmeans.fit_predict(scaled_data)

print("\nHouse Clusters:")
print(df[["Area", "Bedrooms", "Bathrooms", "Age", "Cluster"]])

# --------------------------------
# Display clusters
# --------------------------------

plt.scatter(
    df["Area"],
    df["Price"],
    c=df["Cluster"]
)

plt.xlabel("Area (sq ft)")
plt.ylabel("Price (Lakhs)")
plt.title("House Price Clusters")

plt.show()