# embedded/utils.py

from datetime import datetime

ERROR_LOG = "data/logs/comm_log.txt"

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_error(message):
    timestamp = get_timestamp()
    log_entry = f"[{timestamp}] ERROR: {message}\n"
    with open(ERROR_LOG, "a") as file:
        file.write(log_entry)
