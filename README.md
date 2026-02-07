# UPI-Fraud-Detection
A machine learning–powered UPI fraud detection system that analyzes transaction patterns to identify suspicious and fraudulent activities.
# 🚨 UPI Fraud Detector

A machine learning–powered system to detect **fraudulent UPI (Unified Payments Interface) transactions** in real time or batch mode. This project is designed for **learning, research, hackathons, and portfolio use**, and demonstrates how financial fraud detection systems are built using data analytics and ML.

---

## 📌 Features

* ✅ Detects **fraudulent UPI transactions**
* 📊 Supports **rule-based + ML-based detection**
* ⚡ Real-time & batch prediction support
* 🤖 Uses supervised learning models
* 🧠 Feature engineering inspired by real banking systems
* 📁 Easy-to-understand project structure

---

## 🏗️ System Architecture

```
User / Transaction Stream
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Fraud Detection Engine
   ├── Rule-Based Checks
   └── ML Model Prediction
        ↓
Fraud / Legitimate Output
```

---

## 🧪 Fraud Detection Techniques

### 🔹 Rule-Based Detection

* High transaction amount
* Multiple rapid transactions
* Blacklisted UPI IDs
* Unusual transaction time
* Location mismatch

### 🔹 Machine Learning Models

* Logistic Regression
* Random Forest
* XGBoost (optional)
* Isolation Forest (for anomaly detection)

---

## 📂 Project Structure

```
UPI-Fraud-Detector/
│
├── data/
│   ├── raw_transactions.csv
│   └── processed_data.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── predict.py
│   └── rules.py
│
├── models/
│   └── fraud_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 Features Used for Detection

* Transaction amount
* Transactions per minute
* Sender & receiver risk score
* Time of transaction
* Device ID / IP consistency
* Location variance
* Merchant category

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/UPI-Fraud-Detector.git
cd UPI-Fraud-Detector
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train the Model

```bash
python src/train_model.py
```

### 4️⃣ Run Fraud Detection

```bash
python src/predict.py
```

OR (for web demo)

```bash
python app.py
```

---

## 📈 Model Performance (Sample)

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 96%   |
| Precision | 94%   |
| Recall    | 92%   |
| F1 Score  | 93%   |

---

## ⚠️ Disclaimer

This project uses **synthetic or anonymized data** and is intended **for educational purposes only**. It is **not production-ready** and should not be used directly in real banking systems.

---

## 🔮 Future Enhancements

* 🔐 Integration with live UPI APIs (sandbox)
* 🧾 Graph-based fraud detection
* 🤖 Deep learning (LSTM for transaction sequences)
* 📱 Mobile app integration
* ☁️ Deployment using Docker & Cloud

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Acknowledgements

* RBI & NPCI public fraud reports
* Kaggle fraud datasets
* Scikit-learn documentation

---

## 💬 Contact

Created by Swarup Das
📧 Email: [swarupd15678@gmail.com](mailto:swarupd15678@gmail.com)
🔗 GitHub: [https://github.com/swarupd15678-oss](https://github.com/swarupd15678-oss)

If you like this project, don’t forget to ⭐ the repo!

