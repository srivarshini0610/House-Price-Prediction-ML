
# 🏠 House Price Prediction using Machine Learning

An end-to-end Machine Learning Regression project that predicts residential house prices based on property characteristics such as area, bedrooms, bathrooms, location, furnishing status, parking availability, property age, and nearby amenities.

The project demonstrates the complete machine learning workflow—from data preprocessing and feature engineering to model training, evaluation, and deployment using Streamlit.

---

# 📌 Business Problem

Accurately estimating house prices is one of the biggest challenges in the real estate industry. Buyers often overpay, sellers struggle to price their properties correctly, and agents rely heavily on manual market analysis.

This project builds a Machine Learning model that predicts the estimated selling price of a house using its features, helping users make more informed pricing decisions.

---

# 🎯 Project Objectives

* Predict house prices using supervised machine learning.
* Compare multiple regression algorithms.
* Build a reusable preprocessing pipeline.
* Deploy the trained model through an interactive Streamlit application.
* Demonstrate an end-to-end ML workflow suitable for portfolio and interviews.

---

# 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**
* **Joblib**
* **Streamlit**

---

# 📂 Project Structure

```text
house-price-prediction/
│
├── app.py                     # Streamlit Application
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── house_prices.csv
│
├── models/
│   ├── house_price_model.joblib
│   └── metrics.json
│
├── src/
│   ├── train.py
│   └── eda.py
│
├── images/
│
└── notebooks/
```

---

# 📊 Dataset

The dataset contains property-level information including:

* Area (Square Feet)
* Bedrooms
* Bathrooms
* Stories
* Parking Spaces
* Property Age
* Distance from City
* Location Type
* Furnishing Status
* Main Road Access
* Guest Room
* Basement
* Air Conditioning
* Preferred Area
* House Price (Target)

> **Note:** This repository currently uses a synthetic dataset generated for portfolio purposes. The project can be trained on any real housing dataset with the same schema.

---

# ⚙️ Machine Learning Pipeline

### 1. Data Loading

* Load housing dataset
* Inspect missing values
* Verify data types

### 2. Data Preprocessing

#### Numerical Features

* Median Imputation
* Standard Scaling

#### Categorical Features

* Most Frequent Imputation
* One-Hot Encoding

---

### 3. Train-Test Split

* 80% Training
* 20% Testing

---

### 4. Model Training

The following regression models are trained and compared:

* Linear Regression
* Random Forest Regressor
* Gradient Boosting Regressor

---

### 5. Model Evaluation

Evaluation Metrics:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

The best-performing model is automatically saved for prediction.

---

### 6. Model Deployment

The trained model is deployed using **Streamlit**, allowing users to enter property details and receive an estimated house price instantly.

---

# 🚀 How to Run

## Clone Repository

```bash
git clone https://github.com/yourusername/house-price-prediction.git
```

## Navigate

```bash
cd house-price-prediction
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Train Model

```bash
python src/train.py
```

## Launch Streamlit App

```bash
streamlit run app.py
```

---

# 📈 Model Performance

The training script automatically compares multiple regression algorithms and saves:

* Best Performing Model
* MAE
* RMSE
* R² Score

Results are stored inside:

```text
models/metrics.json
```

---

# 💻 Streamlit Features

* Interactive User Interface
* Property Details Form
* Real-Time Price Prediction
* Automatic Model Loading
* Clean Dashboard Layout

---

# 📚 Skills Demonstrated

* Data Cleaning
* Feature Engineering
* Data Preprocessing
* Machine Learning
* Regression Modeling
* Model Comparison
* Model Evaluation
* Pipeline Creation
* Model Serialization
* Streamlit Deployment
* Python Programming

---

# 🔮 Future Improvements

* Train using a real housing dataset.
* Hyperparameter tuning with GridSearchCV.
* SHAP Explainability for model interpretation.
* Feature Importance Visualization.
* XGBoost and CatBoost integration.
* Model deployment on Streamlit Community Cloud.
* Docker containerization.
* Prediction logging using MySQL.

---

# 📸 Project Screenshots

You can add screenshots here after running the application.

```
images/homepage.png

images/prediction.png

images/result.png
```

---





## ⭐ If you found this project helpful, don't forget to star the repository.

## Author

**Aniket Singh**  
Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning
