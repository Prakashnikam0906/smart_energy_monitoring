# embedded/main.py

import time
import random
from local_storage import save_to_csv
from mqtt_client import send_to_server
from utils import get_timestamp, log_error
# Simulated appliance IDs
APPLIANCES = ["AC001", "WM002", "FR003"]  # Air Conditioner, Washing Machine, Fridge

def simulate_power_usage(device_id):
    if device_id == "AC001":
        return round(random.uniform(1200, 1800), 2)  # Watts
    elif device_id == "WM002":
        return round(random.uniform(500, 1000), 2)
    elif device_id == "FR003":
        return round(random.uniform(100, 300), 2)

def main():
    print("Starting Smart Energy Monitoring Simulation...\n")
    while True:
        try:
            for device in APPLIANCES:
                timestamp = get_timestamp()
                power = simulate_power_usage(device)
                data = {
                    "device_id": device,
                    "timestamp": timestamp,
                    "power": power
                }

                # Store locally
                save_to_csv(data)

                # Send to cloud (simulated server)
                send_to_server(data)

                print(f"[{timestamp}] {device} → {power}W")

            time.sleep(5)  # Wait before next cycle

        except Exception as e:
            log_error(f"Main Loop Error: {str(e)}")
            time.sleep(2)

if __name__ == "__main__":
    main()
