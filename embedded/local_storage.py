# embedded/local_storage.py

import csv
import os
from utils import log_error

LOG_FILE = "data/logs/sensor_log.csv"

# Ensure headers exist
def init_csv():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["device_id", "timestamp", "power"])
            writer.writeheader()

# Save a single record
def save_to_csv(data):
    try:
        init_csv()
        with open(LOG_FILE, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["device_id", "timestamp", "power"])
            writer.writerow(data)
    except Exception as e:
        log_error(f"CSV Write Error: {str(e)}")
