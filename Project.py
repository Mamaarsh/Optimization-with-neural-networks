# Sheduling Algorithm
# FCFS , SJF , RR q = 4
# processes such as pnum and arrrival time and burst time
import pymysql
import numpy as np

# Alghorithm Fcfs
def fcfs(processes):
    n = len(processes)
    waiting_times = [0] * n
    current_time = 0
    for i in range(n):
        arrival_time, burst_time = processes[i]
        if current_time < arrival_time:
            current_time = arrival_time
        waiting_times[i] = current_time - arrival_time
        current_time += burst_time
    return waiting_times

# Alghorithm SJF
def sjf(processes):
    n = len(processes)
    completed = 0
    current_time = 0
    visited = [False] * n
    waiting_times = [0] * n
    while completed < n:
        shortest_index = -1
        shortest_burst = float('inf')
        for i in range(n):
            arrival_time, burst_time = processes[i]
            if arrival_time <= current_time and not visited[i] and burst_time < shortest_burst:
                shortest_burst = burst_time
                shortest_index = i
        if shortest_index == -1:
            current_time += 1
            continue
        arrival_time, burst_time = processes[shortest_index]
        waiting_times[shortest_index] = current_time - arrival_time
        current_time += burst_time
        visited[shortest_index] = True
        completed += 1
    return waiting_times

# Alghorithm RR
def rr(processes, quantum=4):
    n = len(processes)
    remaining_bursts = [burst for (arrival, burst) in processes]
    arrival_times = [arrival for (arrival, burst) in processes]
    waiting_times = [0] * n
    last_execution = arrival_times[:]
    ready_queue = []
    current_time = 0
    completed = 0
    in_queue = [False] * n
    while completed < n:
        for i in range(n):
            if arrival_times[i] <= current_time and remaining_bursts[i] > 0 and not in_queue[i]:
                ready_queue.append(i)
                in_queue[i] = True
        if not ready_queue:
            current_time += 1
            continue
        process_index = ready_queue.pop(0)
        waiting_times[process_index] += current_time - last_execution[process_index]
        execution_time = min(quantum, remaining_bursts[process_index])
        current_time += execution_time
        remaining_bursts[process_index] -= execution_time
        last_execution[process_index] = current_time
        for i in range(n):
            if arrival_times[i] > current_time - execution_time and arrival_times[i] <= current_time and remaining_bursts[i] > 0 and not in_queue[i]:
                ready_queue.append(i)
                in_queue[i] = True
        if remaining_bursts[process_index] > 0:
            ready_queue.append(process_index)
        else:
            completed += 1
    return waiting_times

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='M@m@rsh!a1384_',
    database='OSproj'
)
cursor = conn.cursor()

# 1. فقط یک بار ستون‌ها رو اضافه کن (چک نکنیم اگر هست یا نه برای سادگی):
try:
    cursor.execute("""
    ALTER TABLE dataset
    ADD COLUMN wt_fcfs FLOAT,
    ADD COLUMN wt_sjf FLOAT,
    ADD COLUMN wt_rr FLOAT,
    ADD COLUMN label INT
    """)
    conn.commit()
except:
    # اگر ستون‌ها قبلاً اضافه شده باشن، خطا میده که نادیده می‌گیریمش
    pass

# 2. گرفتن داده‌ها
cursor.execute("SELECT proceses, arrival_time_1, arrival_time_2, arrival_time_3, arrival_time_4, burst_time_1, burst_time_2, burst_time_3, burst_time_4 FROM dataset")
rows = cursor.fetchall()

# 3. محاسبه و آپدیت
for row in rows:
    proceses_id = row[0]
    arrivals = list(row[1:5])
    bursts = list(row[5:9])
    processes = list(zip(arrivals, bursts))

    wt_fcfs = np.mean(fcfs(processes))
    wt_sjf = np.mean(sjf(processes))
    wt_rr = np.mean(rr(processes))

    label = int(np.argmin([wt_fcfs, wt_sjf, wt_rr]))

    update_query = """
    UPDATE dataset SET
        wt_fcfs = %s,
        wt_sjf = %s,
        wt_rr = %s,
        label = %s
    WHERE proceses = %s
    """
    cursor.execute(update_query, (wt_fcfs, wt_sjf, wt_rr, label, proceses_id))

conn.commit()

# 4. آماده‌سازی داده‌ها برای شبکه
X_data = []
y_labels = []

cursor.execute("SELECT arrival_time_1, arrival_time_2, arrival_time_3, arrival_time_4, burst_time_1, burst_time_2, burst_time_3, burst_time_4, label FROM dataset")
rows = cursor.fetchall()

for row in rows:
    X_data.append(row[:8])
    y_labels.append(row[8])

X = np.array(X_data, dtype=np.float32)
y = np.array(y_labels, dtype=np.int64)

conn.close()