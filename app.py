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
# Load and Clean Dataset
# ----------------------------
try:
    df = pd.read_csv("Dataset.csv")
    
    # Clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    # FIX: Force columns to numeric to prevent Matplotlib TypeError
    df["study_hours"] = pd.to_numeric(df["study_hours"], errors='coerce')
    df["student_marks"] = pd.to_numeric(df["student_marks"], errors='coerce')
    
    # FIX: Handle missing values (Mirroring your Colab logic)
    df = df.fillna(df.mean())

except FileNotFoundError:
    st.error("Dataset.csv not found. Make sure the file is in the project root folder.")
    st.stop()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

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
ax.scatter(df["study_hours"], df["student_marks"], color='blue', alpha=0.6)
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
    value=5.0,
    step=0.5
)

if st.button("Predict Marks"):
    # Convert input to DataFrame to keep feature names consistent with training
    input_df = pd.DataFrame([[hours]], columns=["study_hours"])
    prediction = model.predict(input_df)
    
    # Extract prediction value
    # Handles both array and single-value outputs
    predicted_marks = prediction[0][0] if hasattr(prediction[0], "__len__") else prediction[0]
    
    # Ensure marks don't exceed 100 or drop below 0 (Optional logic)
    predicted_marks = max(0, min(100, predicted_marks))
    
    st.success(f"📊 Predicted Marks: {predicted_marks:.2f}/100")

# ----------------------------
# Optional: Show regression line
# ----------------------------
if st.checkbox("Show Regression Line"):
    # Create a range of values for a smooth line
    x_range = np.linspace(df["study_hours"].min(), df["study_hours"].max(), 100).reshape(-1, 1)
    x_range_df = pd.DataFrame(x_range, columns=["study_hours"])
    y_range = model.predict(x_range_df)
    
    fig2, ax2 = plt.subplots()
    ax2.scatter(df["study_hours"], df["student_marks"], color='blue', label='Actual Data', alpha=0.5)
    ax2.plot(x_range, y_range, color='red', linewidth=2, label='Regression Line')
    ax2.set_xlabel("Study Hours")
    ax2.set_ylabel("Student Marks")
    ax2.set_title("Model Fit: Regression Line")
    ax2.legend()
    st.pyplot(fig2)