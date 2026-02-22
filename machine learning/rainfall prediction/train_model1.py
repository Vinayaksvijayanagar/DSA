import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
data = pd.read_csv("weather.csv")

# Columns that contain text
categorical_cols = [
    "WindGustDir",
    "WindDir9am",
    "WindDir3pm",
    "RainToday",
    "RainTomorrow"
]

# Encode categorical columns
le = LabelEncoder()
for col in categorical_cols:
    data[col] = le.fit_transform(data[col])

# Handle missing values
data = data.dropna()

# Features and target
selected_features = [
    "Temp3pm",
    "Humidity3pm",
    "Pressure3pm",
    "WindSpeed3pm",
    "Cloud3pm"
]

X = data[selected_features]
y = data["RainTomorrow"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

# Save model
with open("rainfall_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully!")