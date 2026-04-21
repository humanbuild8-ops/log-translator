from sklearn.ensemble import IsolationForest
import pandas as pd

def categorize_log(level):
    if level == "ERROR":
        return "Critical"
    elif level == "WARNING":
        return "Warning"
    else:
        return "Info"

logs = []

with open('../data/sample_logs.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()

        log_dict = {
            "date": parts[0] + " " + parts[1],
            "time": parts[2],
            "server": parts[3],
            "level": parts[4],
            "category": categorize_log(parts[4]),  # ✅ NEW
            "message": " ".join(parts[5:])
        }

        logs.append(log_dict)

# Print structured logs
for log in logs:
    print(log)

# DataFrame
df = pd.DataFrame(logs)
# Convert category to numeric (ML needs numbers)
df['category_num'] = df['category'].map({
    'Critical': 3,
    'Warning': 2,
    'Info': 1
})

# Create model
model = IsolationForest(contamination=0.2, random_state=42)

# Train + predict
df['anomaly'] = model.fit_predict(df[['category_num']])

# Convert output (-1, 1) to readable form
df['anomaly'] = df['anomaly'].map({
    -1: 'Anomaly',
    1: 'Normal'
})
print("\nDataFrame Output:\n")
print(df)
print("\nAnomaly Detection Output:\n")
print(df[['level', 'category', 'anomaly', 'message']])