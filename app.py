import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Page title
st.title("🎓 Student Marks Prediction App")
st.write("Predict student marks based on study hours")

# Load dataset
df = pd.read_csv("Dataset.csv")

# Show dataset
if st.checkbox("Show Dataset"):
    st.dataframe(df)

# Scatter plot
st.subheader("Study Hours vs Marks")
fig, ax = plt.subplots()
ax.scatter(df.study_hours, df.student_marks)
ax.set_xlabel("Study Hours")
ax.set_ylabel("Student Marks")
st.pyplot(fig)

# Load trained model
model = joblib.load("Students_marks_prediction_model.pkl")

# User input
st.subheader("Enter Study Hours")
hours = st.number_input("Study Hours", min_value=0.0, max_value=24.0, step=0.5)

# Prediction
if st.button("Predict Marks"):
    prediction = model.predict([[hours]])
    st.success(f"📊 Predicted Marks: {prediction[0][0]:.2f}")
