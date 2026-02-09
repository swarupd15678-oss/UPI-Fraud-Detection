#app.py

from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained ML pipeline
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("✅ Model loaded successfully!")

# Serve frontend
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # Build DataFrame EXACTLY as per training data
        input_data = pd.DataFrame([{
            "amount (INR)": data["amount"],
            "transaction type": data["transaction_type"],
            "merchant_category": data["merchant_category"],
            "transaction_status": data["transaction_status"],

            "sender_age_group": data["sender_age_group"],
            "receiver_age_group": data["receiver_age_group"],
            "sender_state": data["sender_state"],

            "sender_bank": data["sender_bank"],
            "receiver_bank": data["receiver_bank"],

            "device_type": data["device_type"],
            "network_type": data["network_type"],

            "hour_of_day": data["hour_of_day"],
            "day_of_week": data["day_of_week"],
            "is_weekend": data["is_weekend"]
        }])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        return jsonify({
            "fraud": int(prediction),
            "probability": f"{round(probability * 100, 2)}%"
        })

    except Exception as e:
        print("❌ Backend error:", e)
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)