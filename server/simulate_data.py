# simulate_data.py

import requests
import random
import time

DEVICE_IDS = ["Device_1", "Device_2", "Device_3"]
SERVER_URL = "http://localhost:5000/energy"

while True:
    device_id = random.choice(DEVICE_IDS)
    power = round(random.uniform(50, 250), 2)

    payload = {
        "device_id": device_id,
        "power": power
    }

    try:
        response = requests.post(SERVER_URL, json=payload)
        if response.status_code == 200:
            print(f"Sent data: {payload}")
        else:
            print(f"Error sending data: {response.text}")
    except Exception as e:
        print(f"Could not connect to server: {e}")

    time.sleep(5)  # Send every 5 seconds
