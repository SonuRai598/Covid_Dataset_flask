import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib

# Loading the dataset
df = pd.read_csv('C:/Users/joges/OneDrive/Desktop/covid dataset/Covid Data.csv')

# Handling missing values
missing_values = df.isnull().sum()
print("Missing values:\n", missing_values[missing_values > 0])

# Updating 'PREGNANT' to No where 'SEX' == Male
df.loc[df['SEX'] == 2, 'PREGNANT'] = 2
print("Updated rows where SEX == 2:\n", df[df['SEX'] == 2])

# Converting 'DATE_DIED' to binary: 1 = died, 2 = alive
df['DATE_DIED'] = df['DATE_DIED'].apply(lambda x: 2 if x == '9999-99-99' else 1)
print("Updated DATE_DIED values:\n", df['DATE_DIED'].value_counts())

df = df.drop('MEDICAL_UNIT', axis=1)

# Shows unique values in each column (excluding 'AGE')
unique_values = df.drop(columns=['AGE']).apply(lambda x: x.unique(), axis=0)
print("\nUnique values in each column (excluding AGE):\n", unique_values)

# Removing rows with values 97, 98, 99 (excluding AGE)
rows_dropped = df.drop(columns=['AGE']).isin([97, 98, 99]).any(axis=1)
df_cleaned = df[~rows_dropped]
print("\nData after removing invalid rows:\n", df_cleaned.info())

# Counting deceased vs alive
count_dead = df_cleaned[df_cleaned['DATE_DIED'] == 1].shape[0]
count_alive = df_cleaned[df_cleaned['DATE_DIED'] == 2].shape[0]
print(f"\nDeceased (1): {count_dead}, Alive (2): {count_alive}")

# Balancing dataset by undersampling alive cases
df_dead = df_cleaned[df_cleaned['DATE_DIED'] == 1]
df_alive = df_cleaned[df_cleaned['DATE_DIED'] == 2].sample(count_dead, random_state=42)
df_balanced = pd.concat([df_dead, df_alive]).sample(frac=1, random_state=42).reset_index(drop=True)
df_balanced = df_balanced.sample(5000, random_state=42)

X = df_balanced.drop('DATE_DIED', axis=1)
Y = df_balanced['DATE_DIED']

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Training SVM model
model = SVC(kernel='linear', probability=True)
model.fit(X_train, Y_train)

# Saving model and scaler 
joblib.dump(model, 'svm_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("\n SVM model and scaler saved successfully.")


