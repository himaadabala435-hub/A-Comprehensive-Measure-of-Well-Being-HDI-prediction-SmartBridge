import numpy as np
from flask import Flask, request, render_template
import pickle

# Initialize the Flask application
app = Flask(__name__)

# Load the trained ML model (Make sure HDI.pkl is in the same folder as app.py)
try:
    model = pickle.load(open("HDI.pkl", "rb"))
except FileNotFoundError:
    print("Warning: 'HDI.pkl' not found in this directory. Make sure you ran your Jupyter Notebook cells successfully!")

@app.route("/")
def home():
    # Renders the initial form interface
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # 1. Grab the values submitted via the HTML form text inputs
    life_input = float(request.form["life"])
    school_input = float(request.form["school"])
    income_input = float(request.form["income"])
    
    # 2. Convert inputs into a 2D NumPy array structure required by scikit-learn
    features = np.array([[life_input, school_input, income_input]])
    
    # 3. Generate the prediction from our loaded model
    prediction = model.predict(features)[0]
    
    # 4. Human Development Index is bound strictly between 0.000 and 1.000
    output = round(max(0.0, min(prediction, 1.0)), 4)
    
    # 5. Send the result text back to the frontend page
    return render_template(
        "index.html",
        prediction_text=f"Predicted Human Development Index: {output}"
    )

if __name__ == "__main__":
    # Runs the local development server
    app.run(debug=True)
