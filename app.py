import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    file_path = "C:/Users/nithi/Downloads/Internship/car_data.csv"
    return pd.read_csv(file_path)

df = load_data()

# Debugging: Display data and statistics
st.write("### Data Sample")
st.write(df.head())

st.write("### Summary Statistics")
st.write(df.describe())

# Ensure Selling_Price is numeric
df["Selling_Price"] = pd.to_numeric(df["Selling_Price"], errors='coerce')

# **1. Improved Histogram**
st.subheader("Distribution of Selling Price 📊")

fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(df["Selling_Price"].dropna(), bins=15, kde=True, color="blue", ax=ax)
ax.set_xlabel("Selling Price (in lakhs)")
ax.set_ylabel("Count")
ax.set_title("Selling Price Distribution")
st.pyplot(fig)

# **2. Boxplot for Outliers**
st.subheader("Boxplot of Selling Price 📦")

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x=df["Selling_Price"].dropna(), color="green", ax=ax)
ax.set_xlabel("Selling Price")
ax.set_title("Boxplot of Selling Price")
st.pyplot(fig)

# **3. Scatter Plot: Selling Price vs Present Price**
st.subheader("Selling Price vs Present Price 💰")

fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(x=df["Present_Price"], y=df["Selling_Price"], hue=df["Fuel_Type"], palette="viridis", ax=ax)
ax.set_xlabel("Present Price (in lakhs)")
ax.set_ylabel("Selling Price (in lakhs)")
ax.set_title("Relationship Between Present and Selling Price")
st.pyplot(fig)
