from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")


def explain(cgpa, coding, projects, internship):
    if cgpa < 6:
        return "⚠ Low CGPA is affecting your chances."
    elif coding < 2:
        return "💻 Improve coding skills for better placement."
    elif projects < 2:
        return "📁 Add more real-world projects."
    elif internship == 0:
        return "🏢 Internship experience increases chances."
    else:
        return "🔥 Strong profile! You are placement ready."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    cgpa = float(request.form["cgpa"])
    aptitude = int(request.form["aptitude"])
    communication = int(request.form["communication"])
    internship = int(request.form["internship"])
    training = int(request.form["training"])
    coding = int(request.form["coding"])
    projects = int(request.form["projects"])

    data = np.array([[cgpa, aptitude, communication, internship, training, coding, projects]])

    prediction = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1] * 100

    if prediction == 1:
        result = "🎉 PLACED"
    else:
        result = "❌ NOT PLACED"

    explanation = explain(cgpa, coding, projects, internship)

    return render_template(
        "result.html",
        prediction=result,
        probability=round(prob, 2),
        explanation=explanation
    )


if __name__ == "__main__":
    app.run(debug=True)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)