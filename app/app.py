import streamlit as st
import pandas as pd
import os
from sklearn.ensemble import IsolationForest
import time

# -------------------------
# Title
# -------------------------
st.title("AI Network Log Translator")
st.markdown("Convert complex network logs into simple human-readable insights with anomaly detection.")
st.markdown("### 📊 Log Analysis Dashboard")
st.divider()
# -------------------------
# Functions
# -------------------------
def categorize_log(level):
    if level == "ERROR":
        return "Critical"
    elif level == "WARNING":
        return "Warning"
    else:
        return "Info"

def generate_explanation(message, category):
    message = message.lower()

    if "cpu" in message:
        return "High CPU usage detected. System performance may degrade."
    elif "disk" in message:
        return "Disk space is running low. Cleanup is recommended."
    elif "packet loss" in message:
        return "Packet loss detected. Network connectivity issues may occur."
    elif "latency" in message:
        return "High latency detected. Users may experience slow responses."
    elif "crash" in message:
        return "Service crash detected. Immediate attention is required."
    else:
        if category == "Critical":
            return "Critical issue detected. Immediate action required."
        elif category == "Warning":
            return "Potential issue detected. Monitoring recommended."
        else:
            return "System is functioning normally."

# -------------------------
# Load Logs
# -------------------------
logs = []

file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_logs.txt')

with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split()

        log_dict = {
            "date": parts[0] + " " + parts[1],
            "time": parts[2],
            "server": parts[3],
            "level": parts[4],
            "category": categorize_log(parts[4]),
            "message": " ".join(parts[5:])
        }

        logs.append(log_dict)

df = pd.DataFrame(logs)

# -------------------------
# Anomaly Detection
# -------------------------
df['category_num'] = df['category'].map({
    'Critical': 3,
    'Warning': 2,
    'Info': 1
})

model = IsolationForest(contamination=0.2, random_state=42)
df['anomaly'] = model.fit_predict(df[['category_num']])

df['anomaly'] = df['anomaly'].map({
    -1: 'Anomaly',
    1: 'Normal'
})

# -------------------------
# AI Explanation
# -------------------------
df['explanation'] = df.apply(
    lambda row: generate_explanation(row['message'], row['category']),
    axis=1
)

# -------------------------
# Summary Metrics
# -------------------------
st.subheader("Summary")

total_logs = len(df)
anomalies = len(df[df['anomaly'] == 'Anomaly'])
critical = len(df[df['category'] == 'Critical'])

st.write(f"Total Logs: {total_logs}")
st.write(f"Anomalies Detected: {anomalies}")
st.write(f"Critical Issues: {critical}")

# -------------------------
# Filter + Display
# -------------------------
st.subheader("🔍 Filtered Log View")

level_filter = st.selectbox("Filter by Level", ["All", "ERROR", "WARNING", "INFO"])

if level_filter != "All":
    filtered_df = df[df['level'] == level_filter]
else:
    filtered_df = df

# -------------------------
# Clean Highlight Function (Readable Colors)
# -------------------------
def highlight_rows(row):
    style = [''] * len(row)

    if row['anomaly'] == 'Anomaly':
        style = ['background-color: #f8d7da; color: black'] * len(row)   # soft red
    elif row['category'] == 'Warning':
        style = ['background-color: #fff3cd; color: black'] * len(row)   # soft yellow
    elif row['category'] == 'Info':
        style = ['background-color: #d1e7dd; color: black'] * len(row)   # soft green

    return style

styled_df = filtered_df[['level', 'category', 'anomaly', 'message', 'explanation']].style.apply(highlight_rows, axis=1)

st.dataframe(styled_df)

# -------------------------
# Show Anomalies
# -------------------------
def generate_incident_summary(df):
    total = len(df)
    critical = len(df[df['category'] == 'Critical'])
    warnings = len(df[df['category'] == 'Warning'])
    anomalies = len(df[df['anomaly'] == 'Anomaly'])

    if anomalies > 0:
        return f"⚠️ {anomalies} anomalies detected. System shows abnormal behavior with {critical} critical issues."
    elif critical > 0:
        return f"🚨 {critical} critical issues detected. Immediate attention recommended."
    elif warnings > 0:
        return f"⚡ {warnings} warnings detected. Monitor system performance."
    else:
        return "✅ System is operating normally with no major issues."

st.subheader("🧠 Incident Summary")
st.info(generate_incident_summary(df))
st.subheader("🚨 Anomalies Detected")

anomaly_df = df[df['anomaly'] == 'Anomaly']

if anomaly_df.empty:
    st.success("No anomalies detected")
else:
    st.error(anomaly_df[['level', 'message', 'explanation']])

start = time.time()

# your processing code

end = time.time()

st.write(f"Time to Clarity: {round(end - start, 2)} seconds")