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
## 📁 Repository Navigation (Tree with Explanation)


Habitability-of-Exoplanets/

│
├── 📁 Dataset/  
│   └── 📄 Exoplanet datasets used for training & preprocessing  
│
├── 📁 static/  
│   ├── 📄 [style.css](static/style.css)  
│   │   └── UI styling (layout, colors, responsiveness)  
│   └── 📄 [chart.js](static/chart.js)  
│       └── Feature visualization using Chart.js  
│
├── 📁 templates/  
│   └── 📄 [index.html](templates/index.html)  
│       └── Frontend UI (input form, prediction display)  
│
├── 📁 venv/  
│   └── 📄 Virtual environment (ignored in Git)  
│
├── 📄 [.gitignore](.gitignore)  
│   └── Git ignore rules  
│
├── 📄 [app.py](app.py)  
│   └── Flask backend, ML inference, API routes  
│
├── 📄 [requirements.txt](requirements.txt)  
│   └── Python dependencies  
│
├── 📄 [LICENSE](LICENSE)  
│   └── MIT License  
│
├── 📄 [README.md](README.md)  
│   └── Project documentation  
│
├── 📄 [exoplanets.db](exoplanets.db)  
│   └── SQLite database storing prediction history  
│
├── 📄 [predictions.csv](predictions.csv)  
│   └── Exported prediction results  
│
├── 📄 [view_db.py](view_db.py)  
│   └── Script to view database records  
│
├── 📄 [feature_columns.pkl](feature_columns.pkl)  
│   └── Stored feature order used during training  
│
├── 📄 [scaler.pkl](scaler.pkl)  
│   └── Trained data scaler  
│
├── 📄 [xgb_habitability_model.pkl](xgb_habitability_model.pkl)  
│   └── Trained XGBoost model  
│
├── 📄 [xgb_habitability_model.json](xgb_habitability_model.json)  
│   └── Model architecture in JSON format  
│
├── 📄 [Confusion-Metrics.png](Confusion-Metrics.png)  
│   └── Model performance visualization  
│
├── 📄 [exoplanet_preprocessed.csv](exoplanet_preprocessed.csv)  
│   └── Cleaned dataset used for training  
│
├── 📄 [ExoPlanet_Habitability.ipynb](ExoPlanet_Habitability.ipynb)  
│   └── EDA and model training notebook  
│
├── 📄 [Habitability.ipynb](Habitability.ipynb)  
│   └── Additional experiments & analysis  
│
└── 📄 [Project learning document.docx](Project%20learning%20document.docx)  
    └── Project notes and learnings

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
  "prediction_label": "Can Survive (Habitable)",
  "habitability_score": 0.88,
  "confidence": "High"
}
```

---


## 📄 License

- This project is licensed under the MIT License.
- See the LICENSE file for details.

---

## Thankings

Special thanks to the **Infosys Springboard Virtual Internship program** and my mentor, **Bhanu Sir**, for their valuable guidance, support, and mentorship throughout this project.

---

## 📬 Contact

Developer: K. Chandrashekar Reddy
GitHub: https://github.com/Chandrashekar0123
