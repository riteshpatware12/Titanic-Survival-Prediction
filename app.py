import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢"
)

st.title("🚢 Titanic Survival Prediction")

st.write(
    "Predict whether a passenger would survive the Titanic disaster."
)

pclass = st.selectbox(
    "Passenger Class",
    [1, 2, 3]
)

sex = st.selectbox(
    "Gender",
    ["male", "female"]
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=25
)

sibsp = st.number_input(
    "Siblings / Spouses Aboard",
    min_value=0,
    value=0
)

parch = st.number_input(
    "Parents / Children Aboard",
    min_value=0,
    value=0
)

fare = st.number_input(
    "Fare",
    min_value=0.0,
    value=50.0
)

embarked = st.selectbox(
    "Embarked",
    ["C", "Q", "S"]
)

if st.button("Predict"):

    input_df = pd.DataFrame({
        'Pclass': [pclass],
        'Sex': [sex],
        'Age': [age],
        'SibSp': [sibsp],
        'Parch': [parch],
        'Fare': [fare],
        'Embarked': [embarked]
    })

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("✅ Passenger Survived")
    else:
        st.error("❌ Passenger Did Not Survive")