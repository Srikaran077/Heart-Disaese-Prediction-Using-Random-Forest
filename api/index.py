from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# Load dataset (303 rows CSV)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "..", "heart.csv")
heart_data = pd.read_csv(CSV_PATH)

X = heart_data.drop(columns="target")
y = heart_data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    values = {}

    if request.method == "POST":
        values = {col: request.form[col] for col in X.columns}
        data = [float(values[col]) for col in X.columns]

        prediction = model.predict([data])[0]

        if prediction == 1:
            result = "⚠️ Heart Disease Detected"
        else:
            result = "✅ No Heart Disease"

    return render_template(
        "index.html",
        result=result,
        values=values
    )

# For local testing with run_local.py
def handler(event, context):
    return app(event, context)
