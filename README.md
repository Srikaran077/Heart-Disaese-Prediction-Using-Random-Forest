# ❤️ Heart Disease Prediction Using Random Forest

This project predicts whether a person has heart disease using a Random Forest machine learning algorithm. The model is trained on medical data and optimized using GridSearchCV for better accuracy.

---

## 📌 Project Overview

Heart disease is a major health problem worldwide. Early prediction can help in timely diagnosis and treatment. This project uses machine learning techniques to analyze patient data and predict the presence of heart disease.

---

## 📂 Dataset

- Dataset file: `heart.csv`
- Target column: `target`
  - 0 → No heart disease
  - 1 → Heart disease present

### Features Used
- age
- sex
- cp
- trestbps
- chol
- fbs
- restecg
- thalach
- exang
- oldpeak
- slope
- ca
- thal

---

## 🧠 Algorithm Used

- Random Forest Classifier
- Ensemble learning technique
- GridSearchCV is used for hyperparameter tuning

---

## ⚙️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn

---

## ▶️ How to Run the Project

### 1. Install Required Libraries
```bash
pip install numpy pandas scikit-learn
```

### Step 2: Install Required Libraries

Open Command Prompt or Terminal and install required libraries:
```
pip install numpy pandas scikit-learn
```
### Step 3: Prepare the Dataset

Ensure the dataset file is named heart.csv

Place it in the same directory as the Python program

### Step 4: Navigate to Project Directory
```
cd Heart-Disease-Prediction-Using-Random-Forest
```
### Run the Python Program
Execute the following command:
```
python heart_disease_prediction.py
```
The program will:
Load and preprocess data
Split data into training and testing sets
Tune hyperparameters using GridSearchCV
Train the Random Forest model
Display accuracy scores

### Step 6: Enter Patient Input Values

Enter values for each medical attribute when prompted.
# Example:
```
Enter age: 52
Enter sex: 1
Enter cp: 0
Enter trestbps: 125
Enter chol: 212
Enter fbs: 0
Enter restecg: 1
Enter thalach: 168
Enter exang: 0
Enter oldpeak: 1.0
Enter slope: 2
Enter ca: 2
Enter thal: 3
```
### Step 7: View Prediction Result

The system will display the result:
```
The person does not have a heart disease.
```
### Model Performance

Training and testing accuracy are displayed after execution

GridSearchCV helps improve model performance

### Sample Output
# High Risk
<img width="500" height="292" alt="image" src="https://github.com/user-attachments/assets/875421ec-cc23-4e84-81e1-1f610a9bcccb" />


# Low Risk
<img width="505" height="297" alt="image" src="https://github.com/user-attachments/assets/4a70c7dc-dd19-47bd-bfd9-2020ea916aab" />

### ✅ Result

The Random Forest model effectively predicts heart disease using patient health parameters.

