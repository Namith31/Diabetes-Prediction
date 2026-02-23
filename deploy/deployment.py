import pandas as pd
import numpy as np
import streamlit as st
import pickle

# load the saved model using pickle
MODEL_PATH = '/workspaces/Diabetes-Prediction/diabetes.sav'
try:
    with open(MODEL_PATH, 'rb') as f:
        loaded_model = pickle.load(f)
except Exception as e:
    st.error(f"Failed to load model: {e}")
    loaded_model = None


def diabetes_prediction(input_data):
    
    
    if loaded_model is None:
        return "Model not loaded"

    
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)

    
    input_data_reshape = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshape)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


def main():
    """Streamlit web app entry point."""
    st.title('Diabetes Prediction Web App')

    st.write('Please enter the following health metrics:')

    # assuming the model was trained on these 14 features
    age = st.number_input('Age', min_value=1, max_value=120, value=30)
    bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=25.0)
    waist_to_hip_ratio = st.number_input('Waist-to-Hip Ratio', min_value=0.0, max_value=5.0, value=0.9)
    systolic_bp = st.number_input('Systolic Blood Pressure', min_value=0.0, max_value=200.0, value=120.0)
    diastolic_bp = st.number_input('Diastolic Blood Pressure', min_value=0.0, max_value=140.0, value=80.0)
    heart_rate = st.number_input('Heart Rate', min_value=0.0, max_value=200.0, value=70.0)
    cholesterol_total = st.number_input('Total Cholesterol', min_value=0.0, max_value=500.0, value=200.0)
    hdl_cholesterol = st.number_input('HDL Cholesterol', min_value=0.0, max_value=200.0, value=50.0)
    ldl_cholesterol = st.number_input('LDL Cholesterol', min_value=0.0, max_value=300.0, value=100.0)
    triglycerides = st.number_input('Triglycerides', min_value=0.0, max_value=1000.0, value=150.0)
    family_history_diabetes = st.selectbox('Family History of Diabetes', options=['No', 'Yes'])
    hypertension_history= st.selectbox('History of Hypertension', options=['No', 'Yes'])
    cardiovascular_history = st.selectbox('History of Cardiovascular Disease', options=['No', 'Yes'])
    dpf = st.number_input('DiabetesPedigreeFunction', min_value=0.0, max_value=2.5, value=0.5)
    

    input_features = [age, bmi, waist_to_hip_ratio, systolic_bp, diastolic_bp, heart_rate,
                      cholesterol_total, hdl_cholesterol, ldl_cholesterol, triglycerides,
                      1 if family_history_diabetes == 'Yes' else 0,
                      1 if hypertension_history == 'Yes' else 0,
                      1 if cardiovascular_history == 'Yes' else 0, dpf]
    if st.button('Predict'):
        result = diabetes_prediction(input_features)
        st.success(result)


if __name__ == '__main__':
    main()

    