# 📦 Project FORESIGHT

AI-Powered Demand Forecasting & Inventory Optimization System

## 📖 Overview

Project FORESIGHT is an end-to-end Data Science project that predicts product demand, identifies inventory risks, and recommends business actions such as Reorder, Markdown, or Healthy stock levels.

The project combines Data Analysis, Machine Learning, and an interactive Streamlit dashboard to help businesses make inventory decisions.

---

## 🚀 Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Forecasting (Random Forest)
- Inventory Risk Scoring
- Interactive Streamlit Dashboard
- SKU Search
- Business Insights

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Streamlit
- Joblib
- Matplotlib

---

## 📂 Project Structure

```text
Project-FORESIGHT/
│
├── app.py
├── README.md
├── requirements.txt
├── models/
├── notebooks/
├── pages/
├── data/
│   ├── raw/
│   └── processed/
└── assets/
```

---

## 📊 Machine Learning Model

**Model:** Random Forest Regressor

### Features Used

- Year
- Month
- Week
- Day
- DayOfWeek
- Lag_1
- Lag_7
- Rolling_7

### Model Performance

| Metric | Value |
|---------|------:|
| MAE | 17.89 |
| RMSE | 68.81 |
| R² Score | 0.372 |

---

## 📈 Dashboard Features

- Revenue Dashboard
- Monthly Revenue Trend
- Inventory Recommendation
- SKU Search
- Inventory Risk Analysis
- Download Risk Report

---

## ▶️ Installation

Clone the repository:

```bash
git clone <your-github-repo-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Dashboard Preview

(Add screenshots after uploading to GitHub.)

---

## 🔮 Future Improvements

- XGBoost Forecasting
- LSTM Time-Series Forecasting
- Live Inventory Database
- Real-time Sales Prediction
- Multi-store Forecasting

---

## 👨‍💻 Developer

**Vicky Sharma**

B.Tech Student

Project developed for learning Data Science, Machine Learning, and Inventory Analytics.

## Note

Large processed datasets and trained ML models are not included because they exceed GitHub's file size limits.

To regenerate them:

1. Run 01_data_loading.ipynb
2. Run 02_EDA.ipynb
3. Run 03_Feature_Engineering.ipynb
4. Run 04_Create_Datasets.ipynb
5. Run 05_Forecasting.ipynb
6. Run 06_Risk_Scoring.ipynb
7. Run 07_ML_Forecasting.ipynb