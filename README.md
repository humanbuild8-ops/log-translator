# 🚀 AI-Powered Network Log Translator

## 📌 Problem Statement

Modern network logs (Syslog, SNMP, VPC Flow Logs) are highly technical and difficult to interpret quickly during incidents.
This increases the **Time to Clarity**, delaying response and increasing downtime.

---

## 💡 Solution

This project builds an **AI-powered pipeline** that transforms raw network logs into:

* Structured data
* Severity classification
* Anomaly detection
* Human-readable insights

👉 Result: **Faster incident understanding and response**

---

## 🧠 Key Features

### 🔹 1. Log Parsing

* Converts raw logs into structured format
* Extracts timestamp, server, level, and message

---

### 🔹 2. Log Categorization

* ERROR → Critical
* WARNING → Warning
* INFO → Informational

---

### 🔹 3. Anomaly Detection (ML)

* Uses **Isolation Forest**
* Detects unusual patterns in log severity
* Flags anomalies in real-time

---

### 🔹 4. AI-Based Log Explanation

* Converts technical logs into simple English
* Helps non-experts understand issues instantly

---

### 🔹 5. 📊 Time to Clarity Metric (CORE INNOVATION)

We measure:

* ⏱️ Time to manually understand logs
* ⚡ Time using our system

👉 **Result: Significant reduction in analysis time**

---

## ⚙️ Tech Stack

* Python
* Pandas
* Scikit-learn (Isolation Forest)
* Streamlit

---

## 🏗️ Architecture

```
Raw Logs → Parser → Structured Data → Categorization → Anomaly Detection → AI Explanation → UI Dashboard
```

---

## 📸 Demo Flow

1. Input raw logs
2. System processes logs
3. Dashboard displays:

   * Severity classification
   * Anomalies
   * Human-readable explanations

---

## 🚀 How to Run

```bash
cd app
python -m streamlit run app.py
```

---

## 📊 Example Output

| Level | Category | Anomaly | Message            | Explanation             |
| ----- | -------- | ------- | ------------------ | ----------------------- |
| ERROR | Critical | Anomaly | CPU usage exceeded | High CPU usage detected |

---

## 🎯 Impact

* Reduces log analysis time
* Improves incident response
* Helps non-experts understand logs

---

## 🔮 Future Improvements

* Real LLM integration (Ollama)
* Real-time log streaming
* Advanced anomaly detection (time-series models)

---

## 👨‍💻 Hack to Horizon

Built for Hack2Hire 1.0 🚀
