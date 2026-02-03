# 🎓 Student Marks Prediction App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg)](https://studentmarksprediction-lalsg5ghbquuji7uebixug.streamlit.app/)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Live Demo
Check out the deployed application here: 
**[Student Marks Prediction Live](https://studentmarksprediction-lalsg5ghbquuji7uebixug.streamlit.app/)**

---

## 📌 Project Overview
This project is a **Supervised Machine Learning** application that predicts a student's marks based on their daily study hours. It demonstrates the full data science lifecycle, from data cleaning and exploratory data analysis (EDA) to model deployment.

The core of the application uses **Simple Linear Regression** to find the relationship between study consistency and academic performance.

## 🛠️ Features
- **Real-time Prediction:** Enter study hours via an interactive slider or input box and get instant grade predictions.
- **Data Visualization:** View the actual dataset via interactive scatter plots.
- **Model Insight:** Toggle the "Regression Line" to see how the mathematical model fits the actual data points.
- **Automated Cleaning:** Handles missing values and data type inconsistencies automatically.

## 💻 Tech Stack
- **Language:** Python
- **Machine Learning:** Scikit-learn (Linear Regression)
- **Data Handling:** Pandas, Numpy
- **Visualization:** Matplotlib
- **App Framework:** Streamlit
- **Model Persistence:** Joblib

## 📊 How it Works
The model follows the linear equation:
$$y = mx + c$$

Where:
* **$y$**: Predicted Student Marks
* **$x$**: Study Hours
* **$m$**: Coefficient (Slope)
* **$c$**: Intercept



## ⚙️ Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ansar-mazhar/Student_Marks_Prediction.git](https://github.com/ansar-mazhar/Student_Marks_Prediction.git)
   cd Student_Marks_Prediction

```

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Run the application:**
```bash
streamlit run app.py

```



## 📂 Project Structure

```text
├── app.py                   # Streamlit application code
├── Dataset.csv              # Student study data
├── Students_marks_prediction_model.pkl # Pre-trained ML model
├── requirements.txt         # Project dependencies
└── student_marks_prediction.ipynb # Original Colab Notebook

```

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improving the model or the UI, feel free to fork the repo and create a pull request.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Developed with ❤️ by [Ansar Mazhar**](https://www.google.com/search?q=https://github.com/ansar-mazhar)

```

---

### How to add this to your project:
1. Create a new file in your project folder named `README.md`.
2. Paste the code above into it.
3. Run these commands to update GitHub:
   ```bash
   git add README.md
   git commit -m "Add professional README"
   git push origin main

```

Would you like me to help you create a **LICENSE** file to go along with this?
