# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import numpy as np

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Student Marks Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Marks Prediction App")
st.write("Predict student marks based on study hours.")

# ----------------------------
# Load Dataset
# ----------------------------
try:
    df = pd.read_csv("Dataset.csv")
except FileNotFoundError:
    st.error("Dataset.csv not found. Make sure the file is in the project root folder.")
    st.stop()

# Clean column names to prevent errors
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Check required columns exist
required_cols = ["study_hours", "student_marks"]
if not all(col in df.columns for col in required_cols):
    st.error(f"Dataset must contain columns: {required_cols}")
    st.stop()

# Optional: show dataset
if st.checkbox("Show Dataset"):
    st.dataframe(df)

# ----------------------------
# Scatter Plot: Study Hours vs Marks
# ----------------------------
st.subheader("Study Hours vs Student Marks")
fig, ax = plt.subplots()
ax.scatter(df["study_hours"], df["student_marks"], color='blue')
ax.set_xlabel("Study Hours")
ax.set_ylabel("Student Marks")
ax.set_title("Study Hours vs Student Marks")
st.pyplot(fig)

# ----------------------------
# Load Trained Model
# ----------------------------
try:
    model = joblib.load("Students_marks_prediction_model.pkl")
except FileNotFoundError:
    st.error("Model file 'Students_marks_prediction_model.pkl' not found.")
    st.stop()

# ----------------------------
# User Input for Prediction
# ----------------------------
st.subheader("Predict Marks")
hours = st.number_input(
    "Enter study hours:",
    min_value=0.0,
    max_value=24.0,
    step=0.5
)

if st.button("Predict Marks"):
    # Predict using model
    prediction = model.predict([[hours]])
    predicted_marks = prediction[0][0]
    st.success(f"📊 Predicted Marks: {predicted_marks:.2f}")

# ----------------------------
# Optional: Show regression line (bonus)
# ----------------------------
if st.checkbox("Show Regression Line"):
    # Predict marks for all study hours in dataset
    x_vals = df[["study_hours"]]
    y_vals = model.predict(x_vals)
    fig2, ax2 = plt.subplots()
    ax2.scatter(df["study_hours"], df["student_marks"], color='blue', label='Actual')
    ax2.plot(df["study_hours"], y_vals, color='red', label='Regression Line')
    ax2.set_xlabel("Study Hours")
    ax2.set_ylabel("Student Marks")
    ax2.set_title("Regression Line vs Actual Data")
    ax2.legend()
    st.pyplot(fig2)
