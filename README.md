# Weather Prediction

A modular machine learning project to **predict weather conditions** based on multiple meteorological features. It includes a complete ML pipeline, model training with MLflow tracking, and a user-friendly Flask web app for real-time prediction. This project is deployed on two Azure platforms for versatility and scalability:
- **Azure App Service** for lightweight web hosting
- **Azure Virtual Machine** using a Docker image pulled from **Azure Container Registry (ACR)**

![Weather data input](/docs/image.png)
![Training info](/docs/image1.jpg)
![Prediction result](/docs/image2.jpg)

---

## Overview

This project utilizes real-time weather data from the **Open-Meteo API** to build a predictive model for classifying weather conditions. The system follows a clean and modular architecture comprising:

- **ETL (Extract, Transform, Load)**
- **Model training and evaluation**
- **Prediction API**
- **Web interface**

---

## Key Features

- **Real-Time Data Ingestion** from Open-Meteo API
- **Preprocessing**: missing value handling, duplicate removal, feature engineering
- **Train-Test Split** with validation metrics
- **ML Model Training** tracked via MLflow
- **Real-Time Predictions** via REST API
- **Flask Web Interface** with HTML/CSS
- **Modular Programming** for reusability and clarity
- **Azure-Based Deployment** with both App Service & Docker VM options
- **GitHub Actions CI/CD** for automated build, test, and deployment workflows

---

## Tech Stack

| Category              | Tools Used                        |
| --------------------- | --------------------------------- |
| Programming Language  | Python                            |
| Web Framework         | Flask                             |
| ML & Tracking         | scikit-learn, MLflow              |
| Data Handling         | Pandas, NumPy                     |
| Data Source           | Open-Meteo API                    |
| Deployment (Web UI)   | Azure App Service                 |
| Deployment (Docker)   | Azure VM via Azure Container Registry |
| CI/CD Automation      | GitHub Actions                    |
| Frontend              | HTML5, CSS3                       |

---

## Input Features

The ML model uses the following meteorological parameters as input:

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

**Target label**: `weather` (e.g., sunny, cloudy, rainy)

---

## Key Steps

### 1. **Data Ingestion**
- Pulls data from Open-Meteo API
- Stores in CSV/JSON for downstream use

### 2. **Data Transformation**
- Cleans missing and duplicate entries
- Engineers new features
- Splits into training/testing datasets

### 3. **Model Training**
- Trains and evaluates ML model
- Logs metrics, hyperparameters, and artifacts using MLflow

### 4. **Prediction**
- Loads trained model
- Accepts new input and returns weather predictions

### 5. **Web Application**
- Flask app provides HTML form for input
- Displays predictions and supports API access

### 6. **CI/CD Pipeline**
- GitHub Actions automates:
  - Code linting and testing
  - Docker image build and push to Azure Container Registry
  - Deployment to Azure App Service and Azure VM
