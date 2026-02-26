# Diabetes Prediction

A machine learning web application that predicts the likelihood of diabetes based on patient health metrics. Built with **scikit-learn** and deployed via **Streamlit**.

---

## Overview

This project trains a classification model on clinical data to predict whether a patient is diabetic or not. The trained model is served through an interactive Streamlit web app where users can input health parameters and receive an instant prediction.

---

## Project Structure

```
Diabetes-Prediction/
│
├── diabettes.sav
├── main.ipynb
├── README.md
│
├── deploy/
│   └── deployment.py
│
└── data/
    └── train.csv
```

| File | Description |
|---|---|
| `diabettes.sav` | Serialized (trained) ML model |
| `main.ipynb` | Model training, EDA & evaluation notebook |
| `README.md` | Project documentation |
| `deploy/deployment.py` | Streamlit web application |
| `data/train.csv` | Dataset used for model training |

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Namith31/Diabetes-Prediction.git
cd Diabetes-Prediction


```

### Run the App

```bash
streamlit run deploy/deployment.py
```

Open your browser at `http://localhost:8501`

## 🧠 Model

- **Algorithm:** *( Random Forest)*
- **Serialization:** `pickle` (`.sav` format)
- **Training details:** See `main.ipynb`