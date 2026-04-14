import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

print("1. Loading dummy house data...")
# A tiny dataset: square footage, bedrooms, and whether it's expensive (0=No, 1=Yes)
data = {
    'square_footage': [1200, 1500, 2500, 3000, 900, 3500],
    'bedrooms': [2, 3, 4, 4, 1, 5],
    'is_expensive': [0, 0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

# Features (Inputs) and Target (Output)
X = df[['square_footage', 'bedrooms']]
y = df['is_expensive']

print("2. Training the Random Forest model...")
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

print("3. Testing model accuracy...")
accuracy = model.score(X, y)
print(f"Model Accuracy: {accuracy * 100}%")

print("4. Saving the trained model...")
# This saves the model into a file so we can use it later!
joblib.dump(model, 'house_model.pkl')
print("Model saved successfully as house_model.pkl!")
