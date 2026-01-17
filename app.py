# ----------------------------
# Routes
# ----------------------------

@app.route("/")
def home():
    # Main UI
    return render_template("index.html")


@app.route("/api")
def api_status():
    # Health check endpoint
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

    # Store in DB
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
