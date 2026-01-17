from flask import Flask, request, jsonify, render_template
import sqlite3
import joblib
import pandas as pd
import os

# ----------------------------
# App Initialization
# ----------------------------
app = Flask(__name__)
API_KEY = "habitability_api_2026"

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "exoplanets.db")

# ----------------------------
# Load ML Components
# ----------------------------
model = joblib.load(os.path.join(BASE_DIR, "xgb_habitability_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
feature_columns = joblib.load(os.path.join(BASE_DIR, "feature_columns.pkl"))

# ----------------------------
# Feature Mapping (UI → Model)
# ----------------------------
FEATURE_MAP = {
    "P_RADIUS": "P_RADIUS",
    "P_MASS": "P_MASS",
    "P_DENSITY": "P_DENSITY_EST",
    "P_SURFACE_TEMP": "P_TYPE_TEMP",
    "P_PERIOD": "P_PERIOD",
    "P_DISTANCE": "P_SEMI_MAJOR_AXIS_EST",
    "S_TYPE": "P_TYPE_TEMP",
    "S_LUMINOSITY": "S_LUMINOSITY",
    "S_TEMPERATURE": "S_TEMPERATURE",
    "S_METALLICITY": "S_METALLICITY"
}

# ----------------------------
# Database Helpers
# ----------------------------
def get_db():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habitability_class INTEGER,
            habitability_score REAL
        )
    """)
    conn.commit()
    conn.close()

create_table()

# ----------------------------
# Prepare Model Input
# ----------------------------
def prepare_input(user_data):
    row = dict.fromkeys(feature_columns, 0)

    for user_key, value in user_data.items():
        if user_key not in FEATURE_MAP:
            return None, f"Invalid feature name: {user_key}"

        model_key = FEATURE_MAP[user_key]
        if model_key in row:
            row[model_key] = value

    df = pd.DataFrame([row])
    df_scaled = scaler.transform(df)
    return df_scaled, None

# ----------------------------
# Routes
# ----------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api_status():
    return jsonify({"status": "API is running"})


@app.route("/predict", methods=["POST"])
def predict():
    if request.headers.get("x-api-key") != API_KEY:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "No JSON data"}), 400

    X, error = prepare_input(data)
    if error:
        return jsonify({"status": "error", "message": error}), 400

    pred_class = int(model.predict(X)[0])
    prob = float(model.predict_proba(X)[0].max())

    rank = "High" if pred_class == 2 else "Medium" if pred_class == 1 else "Low"

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO predictions (habitability_class, habitability_score) VALUES (?, ?)",
        (pred_class, prob)
    )
    conn.commit()
    conn.close()

    return jsonify({
        "status": "success",
        "prediction": pred_class,
        "habitability_score": round(prob, 3),
        "rank": rank
    })


@app.route("/history", methods=["GET"])
def history():
    if request.headers.get("x-api-key") != API_KEY:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM predictions")
    rows = cursor.fetchall()
    conn.close()

    return jsonify({
        "status": "success",
        "count": len(rows),
        "data": rows
    })

# ----------------------------
# Run (Local only)
# ----------------------------
if __name__ == "__main__":
    app.run()
