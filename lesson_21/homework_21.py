from datetime import datetime

def analyze_heartbeat(input_file, output_file):
    TARGET_KEY = "Key TSTFEED0300|7E3E|0400"
    WARNING_THRESHOLD = 31
    ERROR_THRESHOLD = 33

    with open(input_file, "r") as f:
        lines = f.readlines()

    filtered_lines = [line for line in lines if TARGET_KEY in line]

    timestamps = []
    for line in filtered_lines:
        ts_index = line.find("Timestamp ")
        if ts_index != -1:
            ts_str = line[ts_index + len("Timestamp "):ts_index + len("Timestamp ") + 8]
            try:
                ts_obj = datetime.strptime(ts_str, "%H:%M:%S")
                timestamps.append((ts_obj, line.strip()))
            except ValueError:
                pass

    with open(output_file, "w") as log:
        for i in range(len(timestamps) - 1):
            current_time, _ = timestamps[i]
            next_time, _ = timestamps[i + 1]
            diff = (current_time - next_time).total_seconds()
            if diff < 0:  # якщо час перейшов через північ
                diff += 24 * 3600

            if WARNING_THRESHOLD < diff < ERROR_THRESHOLD:
                log.write(f"WARNING: heartbeat = {diff}s at {current_time.time()}\n")
            elif diff >= ERROR_THRESHOLD:
                log.write(f"ERROR: heartbeat = {diff}s at {current_time.time()}\n")

analyze_heartbeat("hblog.txt", "hb_test.log")
