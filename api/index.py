from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static'
)

# Load dataset
heart_data = pd.read_csv('heart.csv')

X = heart_data.drop(columns='target')
Y = heart_data['target']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

model = RandomForestClassifier(random_state=2)
model.fit(X_train, Y_train)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        data = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal'])
        ]

        prediction = model.predict([data])
        result = "⚠️ Heart Disease Detected" if prediction[0] == 1 else "✅ No Heart Disease"

    return render_template('index.html', result=result)

# Required for Vercel
def handler(event, context):
    return app(event, context)
