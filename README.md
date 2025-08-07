# 🦠 COVID-19 Mortality Prediction API

This project uses a Support Vector Machine (SVM) model built on COVID-19 patient data to predict mortality risk. The application is served via a Flask API and allows client-side input for patient data to receive predictions on survival.

---

## 📂 Project Structure

covid_dataset_project/
│
├── app.py # Flask API application
├── request.py # Client-side script to interact with the API
├── model_training.py # Script to clean data and train the SVM model
├── svm_model.pkl # Saved SVM model
├── scaler.pkl # Saved StandardScaler
├── Covid Data.csv # Dataset used for training
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🔧 Installation & Setup

### 1. Clone the Repository

git clone https://github.com/SonuRai598/Covid_Dataset_flask.git
cd Covid_Dataset_flask

2. Create and Activate a Virtual Environment 
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

🚀 How to Run
Step 1: Train the Model
Make sure your dataset is in place (e.g., Covid Data.csv) and run:
python train.py
This will generate svm_model.pkl and scaler.pkl.

Step 2: Start the Flask API Server
python app.py
Flask will start the API at: http://127.0.0.1:5000/predict

Step 3: Run the Client
python request.py
You'll be prompted to enter patient information step by step. The script will send your inputs to the Flask server and return a prediction: "Deceased" or "Alive".

📊 Model Features Used
USMER

SEX

PATIENT_TYPE

INTUBED

PNEUMONIA

AGE

PREGNANT

DIABETES

COPD

ASTHMA

INMSUPR

HIPERTENSION

OTHER_DISEASE

CARDIOVASCULAR

OBESITY

RENAL_CHRONIC

TOBACCO

CLASIFFICATION_FINAL

ICU

Note: The model auto-fixes inconsistencies such as pregnancy input for male patients.

✅ Input Validation Highlights
SEX = Male disables pregnancy input.
Input for yes/no questions only accepts full "yes" or "no".
Numerical fields only accept valid ranges (e.g., classification = 1-7).

