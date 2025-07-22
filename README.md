
# 🧑‍💼 Employee Salary Predictor

This is a machine learning web application that predicts whether an individual's salary is **>50K or <=50K USD** per year based on demographic and employment-related details. The model is trained using the **UCI Adult Income Dataset** and deployed using **Streamlit**.

---

## 🚀 Features

- Input fields for real-world employee attributes
- Uses a **Random Forest Classifier** for accurate predictions
- Clean, interactive UI powered by Streamlit
- Trained and saved as a serialized ML pipeline (`.pkl`)
- Hosted as a fully functional web app

---

## 📊 Dataset

- **Source**: [UCI Machine Learning Repository – Adult Dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- **Attributes**: Age, Workclass, Education Number, Occupation, Race, Capital Gain/Loss, Hours-per-week, etc.
- **Target**: Income (`<=50K` or `>50K`)

---

## 🧠 ML Model

- **Algorithm**: Random Forest Classifier
- **Preprocessing**:
  - Missing value imputation
  - Label encoding (target)
  - One-hot encoding (categorical features)
  - Standard scaling (numerical features)
- **Evaluation Metrics**: Accuracy, Confusion Matrix, Classification Report

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas, NumPy
- Joblib

---

## 💻 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/employee-salary-predictor.git
   cd employee-salary-predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Live Demo

> 🔗 Coming soon...

(Once hosted on [Streamlit Cloud](https://streamlit.io/cloud), add your app URL here.)

---

## 📁 Project Structure

```
employee-salary-predictor/
├── app.py                     # Streamlit app
├── salary_prediction_pipeline.pkl
├── label_encoder.pkl
├── requirements.txt
└── README.md
```

---

## 📄 License

This project is for educational purposes only. You are free to modify and use it for personal or academic learning.

---

## 🙋‍♀️ Author

**S Thejaswini**  

---

⭐ If you found this project helpful, give it a star on GitHub!
