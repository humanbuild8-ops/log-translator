import pandas as pd   # ✅ ADD HERE (top)

logs = []

with open('../data/sample_logs.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()

        log_dict = {
            "date": parts[0] + " " + parts[1],
            "time": parts[2],
            "server": parts[3],
            "level": parts[4],
            "message": " ".join(parts[5:])
        }

        logs.append(log_dict)

# Print structured logs
for log in logs:
    print(log)

# ✅ ADD THIS AT THE END
df = pd.DataFrame(logs)
print("\nDataFrame Output:\n")
print(df)