from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Loading model and scaler
model = joblib.load('svm_model.pkl')
scaler = joblib.load('scaler.pkl')

features = [
    'USMER',
    'SEX',
    'PATIENT_TYPE',
    'INTUBED',
    'PNEUMONIA',
    'AGE',
    'PREGNANT',
    'DIABETES',
    'COPD',
    'ASTHMA',
    'INMSUPR',
    'HIPERTENSION',
    'OTHER_DISEASE',
    'CARDIOVASCULAR',
    'OBESITY',
    'RENAL_CHRONIC',
    'TOBACCO',
    'CLASIFFICATION_FINAL',
    'ICU'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)

        if not all(f in data for f in features):
            missing = [f for f in features if f not in data]
            print("Missing features:", missing)
            return jsonify({'error': 'Missing input features', 'missing': missing}), 400

        X = np.array([float(data[f]) for f in features]).reshape(1, -1)
        print("Feature array shape:", X.shape)
        
        X_scaled = scaler.transform(X)
        print("Scaled features:", X_scaled)

        prediction = model.predict(X_scaled)[0]
        result = "Deceased" if prediction == 1 else "Alive"
        return jsonify({'prediction': result})

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'Something went wrong', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

