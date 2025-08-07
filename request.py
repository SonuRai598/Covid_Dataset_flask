import requests

def get_binary_input(prompt):
    while True:
        value = input(prompt + " (yes/no): ").strip().lower()
        if value == "yes":
            return 1
        elif value == "no":
            return 2
        else:
            print(" Please enter 'yes' or 'no' only.")

def get_choice_input(prompt, choices):
    while True:
        try:
            value = int(input(f"{prompt} ({'/'.join(map(str, choices))}): ").strip())
            if value in choices:
                return value
            else:
                print(f" Please enter one of the valid choices: {choices}")
        except ValueError:
            print(" Invalid input. Please enter a number.")

def get_positive_number(prompt):
    while True:
        try:
            value = int(input(prompt + ": ").strip())
            if value >= 0:
                return value
            else:
                print(" Please enter a non-negative number.")
        except ValueError:
            print(" Invalid input. Please enter a number.")

# Collecting input from user
print(" Please answer the following questions about the patient:")

user_data = {}

user_data['USMER'] = get_choice_input("Level of medical unit patient treated", [1, 2, 3])
user_data['SEX'] = get_choice_input("Sex of the patient (1 = Female, 2 = Male)", [1, 2])
user_data['PATIENT_TYPE'] = get_choice_input("Type of care received (1 = Returned home, 2 = Hospitalization)", [1, 2])
user_data['INTUBED'] = get_binary_input("Was the patient connected to a ventilator?")
user_data['PNEUMONIA'] = get_binary_input("Does the patient have pneumonia?")
user_data['AGE'] = get_positive_number("Age of the patient")

# Asking pregnancy only for females
if user_data['SEX'] == 1:
    if user_data['AGE'] < 10:
        print("Note: Patient is under 10. Please confirm pregnancy status carefully.")
    user_data['PREGNANT'] = get_binary_input("Is the patient pregnant?")
else:
    user_data['PREGNANT'] = 2  # Not pregnant if male

user_data['DIABETES'] = get_binary_input("Does the patient have diabetes?")
user_data['COPD'] = get_binary_input("Does the patient have chronic obstructive pulmonary disease?")
user_data['ASTHMA'] = get_binary_input("Does the patient have asthma?")
user_data['INMSUPR'] = get_binary_input("Is the patient immunosuppressed?")
user_data['HIPERTENSION'] = get_binary_input("Does the patient have hypertension?")
user_data['OTHER_DISEASE'] = get_binary_input("Does the patient have any other disease?")
user_data['CARDIOVASCULAR'] = get_binary_input("Does the patient have cardiovascular disease?")
user_data['OBESITY'] = get_binary_input("Is the patient obese?")
user_data['RENAL_CHRONIC'] = get_binary_input("Does the patient have chronic renal disease?")
user_data['TOBACCO'] = get_binary_input("Is the patient a tobacco user?")
user_data['CLASIFFICATION_FINAL'] = get_choice_input("COVID test result classification (1-3 = positive, 4+ = negative)", [1, 2, 3, 4, 5, 6, 7])
user_data['ICU'] = get_binary_input("Was the patient admitted to ICU?")

# Sending POST request to the API
url = 'http://127.0.0.1:5000/predict'
response = requests.post(url, json=user_data)

# result
print("\n Prediction result from API:")
if response.status_code == 200:
    print(response.json())
else:
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")

    

