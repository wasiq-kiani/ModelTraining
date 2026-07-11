import streamlit as st
import joblib
import pandas as pd

# 1. Page layout configuration
st.title("Machine Learning Prediction App")
st.write("Enter your data below to get an instant prediction.")


# 2. Cached model loading function using joblib
@st.cache_resource
def load_model():
    # Recommended file extensions for joblib: .joblib, .pkl, or .pkl.z
    return joblib.load("Student_Performance_Model.joblib")


model = load_model()

# 3. Build user inputs for your features
st.subheader("Input Features")
Hours_Studied= st.number_input("Hours Studied:", min_value=0, max_value=10)
Previous_Scores = st.number_input("Previous Scores:", min_value=0, max_value=100)
Sleep_Hours = st.number_input("Sleep Hours:", min_value=0, max_value=24)
Practiced_Papers = st.number_input("Sample Question Papers Practiced:", min_value=0, max_value=10)

# 4. Convert inputs into a pandas DataFrame
# Ensure dictionary keys match your model's training column names exactly
input_data = pd.DataFrame([{
    "Hours Studied": Hours_Studied,
    "Previous Scores": Previous_Scores,
    "Sleep Hours": Sleep_Hours,
    "Sample Question Papers Practiced": Practiced_Papers
}])

# Display the prepared dataframe in the UI for visibility
st.write("Formatted Input Data:", input_data)

# 5. Run prediction when button is clicked
if st.button("Generate Prediction"):
    prediction = model.predict(input_data)

    st.subheader("Result:")
    st.success(f"The model predicted value is: {prediction[0]}")
