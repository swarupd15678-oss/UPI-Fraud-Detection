<h1 align="center">🚨 UPI Fraud Detection System</h1>
A Machine Learning–powered web application that detects potentially fraudulent UPI transactions in real time.
Built using Python, Flask, Scikit-learn, Bootstrap, and JavaScript, this system takes transaction details from a user-friendly UI and predicts whether the transaction is Safe or Fraudulent, along with a risk probability.

📌 Features

✅ Real-time fraud prediction

📊 Machine Learning classification model

🌐 Interactive web interface (Bootstrap 5)

🔄 REST API (/predict) for model inference

🧠 Uses transaction behavior, user demographics, device & network info

📈 Returns fraud probability score

🛠️ Tech Stack
Frontend

HTML5

CSS3

Bootstrap 5

JavaScript (Fetch API)

Backend

Python

Flask

Pandas

Scikit-learn

Pickle (model serialization)

Machine Learning

Supervised Classification Model

Trained on synthetic UPI transaction dataset (2024)

<h2>📂 Project Structure</h2>
<pre>
upi-fraud-detection/
│
├── app.py                 # Flask backend
├── model.pkl              # Trained ML pipeline
├── requirements.txt       # Python dependencies
│
├── templates/
│   └── index.html         # Frontend UI
│
├── static/
│   └── app.css            # Custom styling
│
├── dataset/
│   └── upi_transactions_2024.csv
│
└── README.md
📊 Dataset Description
</pre>
The model is trained on a UPI transaction dataset containing features such as:

Transaction amount (INR)

Transaction type (P2P / P2M)

Merchant category

Transaction status

Sender & receiver age group

Sender state

Sender & receiver bank

Device type (New / Old)

Network type (4G / 5G / WiFi)

Time-based features:

Hour of day

Day of week

Weekend indicator

Target variable:

fraud (0 = Safe, 1 = Fraud)

🚀 How to Run Locally

1️⃣ Clone the Repository
git clone https://github.com/swarupd15678-oss/upi-fraud-detection.git
cd upi-fraud-detection

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Flask App
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000/
🔌 API Endpoint
POST /predict

Request (JSON):

{
  "amount": 5000,
  
  "transaction_type": "P2P",
  
  "merchant_category": "Retail",
  
  "transaction_status": "Success",
  
  "sender_age_group": "26-35",
  
  "receiver_age_group": "36-45",
  
  "sender_state": "Maharashtra",
  
  "sender_bank": "SBI",
  
  "receiver_bank": "HDFC",
  
  "device_type": "Old",
  
  "network_type": "4G",
  
  "hour_of_day": 14,
  
  "day_of_week": "Monday",
  
  "is_weekend": 0
  
}

Response:

{
  "fraud": 1,
  "probability": "87.32%"
}
🖥️ User Interface Preview

Clean single-page UI

Dropdowns for categorical inputs

Automatic time & day detection

Fraud result highlighted with color:

🟢 Green → Safe Transaction

🔴 Red → Fraud Detected

⚠️ Disclaimer

This project is intended for educational and demonstration purposes only.
It should not be used as a production-grade fraud detection system without further validation, security hardening, and regulatory compliance.

📌 Future Enhancements

🔐 User authentication

📊 Transaction history dashboard

🧠 Deep learning model

🌍 Geo-location based risk analysis

☁️ Cloud deployment (AWS / GCP / Azure)

👤 Author

Created By Codecrafters👨‍💻 

🎓 B.Tech

💡 Machine Learning & Data Enthusiastics

