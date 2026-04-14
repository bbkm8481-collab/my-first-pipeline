from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the brain
model = joblib.load('house_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the user
    data = request.get_json()
    square_footage = data['square_footage']
    bedrooms = data['bedrooms']
    
    # Ask the model for a prediction
    prediction = model.predict([[square_footage, bedrooms]])
    
    # Send the answer back (0 = Not Expensive, 1 = Expensive)
    result = "Expensive" if prediction[0] == 1 else "Not Expensive"
    return jsonify({'Prediction': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)