# Weather Prediction

A modular machine learning project to **predict weather conditions** based on multiple meteorological features. It includes complete data pipelines, model training with MLflow tracking, and a user-friendly Flask web app to input data and get predictions.

---

## Overview

This project uses real-time weather data from the **Open-Meteo API** to build a predictive model for weather conditions. It emphasizes clean architecture through modular pipelines: 
- **ETL (Extract, Transform, Load)**
- **Model training and evaluation**
- **Prediction API**

The web interface allows users to submit key environmental variables and view predictions instantly.

---

## Key Features

- **Data Ingestion** from Open-Meteo API
- **Data Preprocessing**: handle missing values, remove duplicates, and feature engineering
- **Train-Test Splitting** for model validation
- **Model Training and Evaluation** with MLflow logging
- **Prediction Pipeline** for real-time inference
- **Flask Web App** with HTML/CSS UI and REST API
- **Modular Programming** for better structure and reusability

---

## 🛠️ Tech Stack

| Category         | Tools Used                         |
|------------------|------------------------------------|
| Programming Languange | Python                             |
| Web Framework    | Flask                              |
| ML & Tracking    | scikit-learn, MLflow               |
| Data Handling    | Pandas, NumPy                      |
| Data Source      | Open-Meteo API                     |
| Frontend         | HTML5, CSS3                        |


---

## Input Features

The model is trained using the following features:

- `temperature_2m_max`
- `temperature_2m_min`
- `apparent_temperature_max`
- `apparent_temperature_min`
- `wind_speed_10m_max`
- `wind_gusts_10m_max`
- `wind_direction_10m_dominant`
- `shortwave_radiation_sum`
- `uv_index_max`
- `daylight_duration`
- `sunshine_duration`
- `et0_fao_evapotranspiration`

**Target label**: `weather`

---

## Key Steps

### 1. **Data Ingestion**
- Extract weather data using Open-Meteo API
- Store and format it for further processing

### 2. **Data Transformation**
- Handle missing values
- Remove duplicate records
- Apply feature engineering
- Split into training and testing sets

### 3. **Model Training**
- Train a machine learning model
- Log metrics and parameters with MLflow
- Evaluate accuracy and performance

### 4. **Prediction**
- Load trained model
- Predict weather based on new inputs

### 5. **Flask Web Application**
- Input data through a styled form
- View predictions on submit
- Re-train model with a dedicated route

---
