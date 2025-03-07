# 🚗 Car Price Prediction Analysis

This project is a **Machine Learning** model to predict car selling prices based on various factors such as age, fuel type, transmission, and kilometers driven. It uses **Streamlit** for a user-friendly web interface.

## 📌 Features

- **Data Cleaning & Preprocessing:** Handling missing values, encoding categorical data, and feature scaling.
- **Exploratory Data Analysis (EDA):** Visualizations to understand trends and relationships.
- **Machine Learning Model:** Trained using regression techniques to predict car prices.
- **Interactive Web App:** Built with **Streamlit** to make predictions based on user input.

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/nithinpawar10/Car_Price-Prediction-Analysis.git
cd Car_Price-Prediction-Analysis


2️⃣ Install Dependencies
Ensure you have Python 3.7+ installed. Then, install the required libraries:

sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Streamlit App
sh
Copy
Edit
streamlit run app.py
This will launch the web app in your browser.

📊 Dataset
The dataset includes the following features:

Year: Year of car purchase.
Selling_Price: Price at which the car was sold.
Present_Price: Current market price.
Fuel_Type: Type of fuel (Petrol/Diesel/CNG).
Kms_Driven: Total kilometers driven.
Transmission: Manual or Automatic.
Owner: Number of previous owners.
Ensure the dataset (car_data.csv) is present in the project directory.
