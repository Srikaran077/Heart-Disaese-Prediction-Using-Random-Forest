# ❤️ Heart Disease Prediction Using Random Forest

## 📌 Project Overview
Heart disease is one of the major health problems worldwide. Early prediction can help in preventing serious complications.  
This project predicts whether a person has heart disease using a **Random Forest Machine Learning model** and provides results through a **Flask-based web application**.

The system integrates **Machine Learning + Web Development** to create an end-to-end predictive application.

---

## 🎯 Objectives
- To predict the risk of heart disease using medical parameters  
- To build a user-friendly web interface for prediction  
- To integrate a machine learning model with Flask  
- To demonstrate a complete ML mini project  

---

## 🧠 Machine Learning Model
- **Algorithm:** Random Forest Classifier  
- **Why Random Forest?**
  - High accuracy
  - Handles non-linear data
  - Reduces overfitting
  - Suitable for medical datasets  

---

## 📊 Dataset Information
- **Dataset Name:** Heart Disease Dataset  
- **Total Features:** 13  
- **Target Column:** `target`  
  - `0` → No Heart Disease  
  - `1` → Heart Disease  

### Input Features:
1. Age  
2. Sex  
3. Chest Pain Type (cp)  
4. Resting Blood Pressure (trestbps)  
5. Cholesterol (chol)  
6. Fasting Blood Sugar (fbs)  
7. Resting ECG (restecg)  
8. Maximum Heart Rate (thalach)  
9. Exercise Induced Angina (exang)  
10. Oldpeak  
11. Slope  
12. Number of Major Vessels (ca)  
13. Thalassemia (thal)  

---

## 🖥️ Technologies Used

| Category | Tools |
|--------|-------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Web Framework | Flask |
| Frontend | HTML, CSS |
| Version Control | Git, GitHub |

---

## 🏗️ Project Structure

heart-disease-prediction/
│
├── app.py
├── heart.csv
├── requirements.txt
├── README.md
│
├── templates/
│ └── index.html
│
└── static/
└── style.css


---

## ⚙️ Working of the System
1. User enters medical details in the web form  
2. Flask collects the input data  
3. The Random Forest model processes the data  
4. Prediction result is generated  
5. Result is displayed on the web page  

---

## ▶️ How to Run the Project

### Step 1: Install Required Packages
```bash
pip install -r requirements.txt
```
### Step 2: Run Flask Application
```
python app.py
```
### Step 3: Open Browser
http://127.0.0.1:5000/

## 📈 Model Performance

Training Accuracy: ~100%

Testing Accuracy: ~66%

Note: Slight overfitting is expected due to small dataset size and is acceptable for academic projects.

## ✅ Output

No Heart Disease
<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/7a8d4663-0d57-4cdd-8cc2-d3a9ee157a6e" />

Heart Disease Detected
<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/9836e8d5-acc9-42eb-9dee-c50c4afa3d62" />

The result is displayed immediately after submitting the form.


## ✅ Result
The Random Forest model effectively predicts heart disease using patient health parameters.
