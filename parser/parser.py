file = open('../data/sample_logs.txt', 'r')
logs = file.readlines()

for log in logs:
    print(log.strip())