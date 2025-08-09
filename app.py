import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('model.pkl')

st.title("Credit Card Fraud Detection")

st.write("Upload your transaction CSV file for fraud prediction.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded data preview:")
    st.dataframe(data.head())

    # Check if features are present (adjust based on your dataset)
    if 'Class' in data.columns:
        data = data.drop('Class', axis=1)  # Remove label if present

    # Predict
    predictions = model.predict(data)
    data['Fraud_Prediction'] = predictions

    st.write("Prediction Results:")
    st.dataframe(data)

    # Download results
    csv = data.to_csv(index=False).encode()
    st.download_button(
        label="Download predictions as CSV",
        data=csv,
        file_name='fraud_predictions.csv',
        mime='text/csv',
    )

