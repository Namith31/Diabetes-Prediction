Diabetes Prediction Web App

A Machine Learning–powered Diabetes Prediction System built using Python, Streamlit, and Scikit-learn.
This application allows users to input medical parameters and get an instant prediction on whether they are diabetic or not.

Project Overview

Diabetes is one of the most common chronic diseases worldwide.
This project uses a trained ML model to predict diabetes risk based on health-related inputs such as glucose level, BMI, age, etc.

The app provides a simple web interface for real-time predictions.

Machine Learning Workflow

Data Collection (kaggle compltion Diabetes Dataset)

Data Preprocessing

Feature Selection

Model Training (Random Forest classification)

Model Serialization using pickle

Deployment using Streamlit

Real-time Prediction via Web App

Diabetes-Prediction/
│
├── diabettes.sav          # Saved trained ML model
├── main.ipynb             # Model training notebook
├── README.md              # Project documentation
│
├── deploy/
│   └── deployment.py      # Streamlit web application
│
├── data/
│   └── train.csv          # Training dataset


Run the Streamlit App
streamlit run deploy/deployment.py

