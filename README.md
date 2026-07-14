# Human Development Index (HDI) Prediction using Machine Learning

## 📌 Project Summary

**Human Development Index (HDI) Prediction** is a Machine Learning-based web application developed to predict the Human Development Index (HDI) using key socio-economic indicators. The application automates the prediction process by analyzing important factors such as **Life Expectancy at Birth, Expected Years of Schooling, and Gross National Income (GNI) per Capita** using a trained Linear Regression model.

Instead of manually calculating the HDI, the system predicts the HDI instantly through a user-friendly web interface, making it useful for researchers, students, policymakers, and data analysts.

The application is built using **Python, Machine Learning, Flask, HTML, CSS, and JavaScript**, providing an easy and interactive platform for HDI prediction.

---

# ✨ Key Features

* Predicts Human Development Index (HDI) instantly
* Machine Learning-based prediction using Linear Regression
* User-friendly Flask web application
* Real-time prediction based on user inputs
* Responsive and interactive web interface
* Displays predicted HDI score
* Input validation for accurate predictions
* Lightweight and fast prediction system
* Easy deployment using Flask
* Simple interface suitable for educational and research purposes

---

# 🏗 Technical Architecture

The project follows a **three-layer architecture**.

### 1. Machine Learning Layer

Responsible for:

* Loading the HDI dataset
* Data preprocessing
* Feature selection
* Training the Linear Regression model
* Saving the trained model as **HDI.pkl**

---

### 2. Backend Layer

Implemented using **Flask**.

Responsible for:

* Handling HTTP requests
* Loading the trained ML model
* Accepting user input
* Performing HDI prediction
* Returning prediction results to the frontend

---

### 3. Presentation Layer

Developed using:

* HTML5
* CSS3
* Flask Templates (Jinja2)

Provides:

* Input form for HDI indicators
* Prediction button
* Result display page
* Clean and responsive user interface

---

# 👤 Project Submitted By

**Jahnavi Senagana** - Team Member - johnavisenagana25@gmail.com
---
 Hima Adabala - Team Leader - himaadabala435@gmail.com
---
 Kopparthi Mahesh Pani - Team Member - kopparthimahesh3458@gmail.com
---
 Nageswari Koppisetti - Team Member - koppisettinageswari803@gmail.com
---


Department of Electronics and Communication Engineering (ECE)

Swarnandhra College of Engineering and Technology

---

# 🚀 How to Run the Application

## Prerequisites

Before running the project, ensure you have:

* Python 3.10 or higher
* pip package manager
* VS Code or any Python IDE

---

## Step 1: Navigate to the Project Folder

Open the terminal and move to the project directory.

```bash
cd HumanDevelopmentIndex
```

---

## Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Step 4: Train the Machine Learning Model

Run the Jupyter Notebook or Python training script to train the Linear Regression model and generate the model file.

```bash
python HumDevIndex.py
```

or execute all cells in

```
HumDevIndex.ipynb
```

After successful training,

```
HDI.pkl
```

will be generated inside the Flask project folder.

---

## Step 5: Launch the Flask Application

Run

```bash
python app.py
```

---

## Step 6: Open the Application

Visit:

```
http://127.0.0.1:5000
```

---

# 🧪 Testing (Optional)

Verify that the application predicts the HDI correctly by entering sample values for:

* Life Expectancy at Birth
* Expected Years of Schooling
* Gross National Income (GNI)

Click **Predict HDI** and verify that the predicted HDI score is displayed.

---

# 📂 Project Structure

```
HumanDevelopmentIndex/
│
├── Dataset/
│   └── HDI.csv
│
├── Flask/
│   ├── static/
│   │   └── style.css
│   │
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   │
│   ├── app.py
│   ├── HDI.pkl
│   └── requirements.txt
│
├── Training/
│   └── HumDevIndex.ipynb
│
└── README.md
```

---

# 🛠 Technologies Used

* Python
* Machine Learning
* Linear Regression
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML5
* CSS3
* Jupyter Notebook
* VS Code

---

# 📊 Input Features

The model predicts HDI using the following three features:

* Life Expectancy at Birth
* Expected Years of Schooling
* Gross National Income (GNI) per Capita

---

# 📈 Output

The application predicts:

* Human Development Index (HDI) Score

The predicted value is displayed instantly on the webpage after clicking the **Predict HDI** button.
