# 🌍 Habitability of Exoplanets — Machine Learning Predictor

A full-stack machine learning project that predicts whether an exoplanet is potentially **habitable**, **not habitable**, or **uncertain** based on its planetary and stellar parameters.  
The project includes a **trained model**, a **Flask API**, and a **web UI** deployed on Render — making predictions interactive and accessible.

---

## 📌 🔍 Project Summary

Planets orbiting stars other than the Sun — called **exoplanets** — are constantly being discovered. Some of these may occupy the “habitable zone” where conditions could support life. This project:

- Uses real exoplanet data to train a machine learning model.
- Serves the model through a Flask backend API.
- Provides a responsive frontend where users can input exoplanet features and receive a prediction with a confidence score.
- Is deployed and accessible via a live web application.

🧠 The model classifies exoplanets into:
- **Can Survive (Habitable)**
- **Cannot Survive (Not Habitable)**
- **Cannot Define Clearly (Uncertain)**

---

## 🛠️ Features

✨ **ML-powered prediction** based on planetary characteristics  
🌐 **Interactive web frontend** for user input  
🧾 **Backend API** for integration or automation  
📊 **Feature value bar chart visualization**  
📦 Fully deployable using Render

---

## 🚀 Live Demo

Your live deployed application is available at:  
➡️ **https://habitability-of-exoplanets-hl2e.onrender.com/**

---

## ⚙️ Installation Setup (Local)

Follow these steps to set up the project locally:

1. **Clone the repository**

   ```bash
   git clone https://github.com/Chandrashekar0123/Habitability-of-Exoplanets.git
   cd Habitability-of-Exoplanets

2. **Create a virtual environment**
   
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the app

```bash
python app.py
```


**The server will start and be available at http://127.0.0.1:5000/.**

---

## 🧩 How to Use

### 🧪 Using the Web UI

1. Open the application homepage.
2. Enter all required **planetary and stellar parameters**.
3. Click **Predict Habitability**.
4. The UI displays:
   - **Prediction** (Can Survive / Cannot Survive / Cannot Define Clearly)
   - **Habitability Score**
   - **Confidence level**
   - **Feature value bar chart**

---

### 📡 Using the API

**Endpoint**
**POST /predict**


**Headers**
```json
{
  "Content-Type": "application/json",
  "x-api-key": "habitability_api_2026"
}
```

**Request Body (Example)**

```
{
  "P_RADIUS": 1.0,
  "P_MASS": 1.1,
  "P_DENSITY": 5.5,
  "P_SURFACE_TEMP": 288,
  "P_PERIOD": 365,
  "P_DISTANCE": 1.0,
  "S_TYPE": 1,
  "S_LUMINOSITY": 1.0,
  "S_TEMPERATURE": 5800,
  "S_METALLICITY": 0.02
}
```

**Response (Example)**
```
{
  "status": "success",
  "prediction_label": "Can Survive (Habitable)",
  "habitability_score": 0.88,
  "confidence": "High"
}
```

---

## 📁 Project Structure & Navigation

Habitability-of-Exoplanets/
│
├── app.py
│   ├─ Flask backend
│   ├─ ML model loading & inference
│   ├─ API routes (/predict, /history)
│   └─ UI rendering
│
├── requirements.txt
│   └─ Project dependencies
│
├── exoplanets.db
│   └─ SQLite database storing predictions
│
├── xgb_habitability_model.pkl
├── scaler.pkl
├── feature_columns.pkl
│   └─ Trained ML artifacts
│
├── templates/
│   └── index.html
│       └─ Web UI for habitability prediction
│
├── static/
│   ├── style.css
│   │   └─ UI styling
│   └── chart.js
│       └─ Feature visualization (Chart.js)
│
└── Dataset/
    └── Exoplanet datasets



*This structure cleanly separates backend logic, machine learning artifacts, UI, and datasets, making the project easy to understand, maintain, and extend.*


## 📄 License

This project is licensed under the MIT License.
See the LICENSE file for details.

## 📬 Contact

Developer: K. Chandrashekar Reddy
GitHub: https://github.com/Chandrashekar0123
