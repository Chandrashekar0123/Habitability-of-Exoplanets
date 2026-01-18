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

