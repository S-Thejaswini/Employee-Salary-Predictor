import streamlit as st
import pandas as pd
import joblib

# Load the saved model and encoder
model = joblib.load("salary_prediction_pipeline.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Title
st.title("🧑‍💼 Employee Salary Prediction")
st.write("Predict whether an individual's income is >50K or <=50K based on demographic info.")

# Input form
with st.form("prediction_form"):
    st.subheader("Enter Employee Details:")

    age = st.number_input("Age", min_value=17, max_value=75, value=30)
    workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Local-gov', 'State-gov', 'Federal-gov', 'Self-emp-inc', 'Without-pay', 'Never-worked'])
    fnlwgt = st.number_input("FNLWGT", min_value=10000, max_value=1000000, value=200000)
    education_num = st.slider("Education Number", 1, 16, 10)
    marital_status = st.selectbox("Marital Status", ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent'])
    occupation = st.selectbox("Occupation", ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty',
                                             'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving',
                                             'Priv-house-serv', 'Protective-serv', 'Armed-Forces'])
    relationship = st.selectbox("Relationship", ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'])
    race = st.selectbox("Race", ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'])
    gender = st.radio("Gender", ['Male', 'Female'])
    capital_gain = st.number_input("Capital Gain", 0, 100000, 0)
    capital_loss = st.number_input("Capital Loss", 0, 100000, 0)
    hours_per_week = st.slider("Hours per Week", 1, 100, 40)
    native_country = st.selectbox("Native Country", ['United-States', 'Mexico', 'Philippines', 'Germany', 'Canada', 'India', 'England', 'China', 'Cuba', 'Other'])

    submit = st.form_submit_button("Predict Salary Range")

# Prediction
if submit:
    input_df = pd.DataFrame({
        'age': [age],
        'workclass': [workclass],
        'fnlwgt': [fnlwgt],
        'educational-num': [education_num],
        'marital-status': [marital_status],
        'occupation': [occupation],
        'relationship': [relationship],
        'race': [race],
        'gender': [gender],
        'capital-gain': [capital_gain],
        'capital-loss': [capital_loss],
        'hours-per-week': [hours_per_week],
        'native-country': [native_country]
    })

    prediction = model.predict(input_df)
    result = label_encoder.inverse_transform(prediction)[0]

    st.success(f"💼 Predicted Income: **{result}**")
