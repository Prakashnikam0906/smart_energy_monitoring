import csv
import sys

def query_device(device_id, csv_path='data/logs/sensor_log.csv'):
    power_values = []
    last_reading = None

    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['device_id'] == device_id:
                power_values.append(float(row['power']))
                last_reading = row

    if power_values:
        print(f"\n🔌 Details for Device: {device_id}")
        print(f"Latest Reading: {last_reading['timestamp']} — {last_reading['power']}W")
        print(f"Average Power: {sum(power_values)/len(power_values):.2f}W")
        print(f"Max Power: {max(power_values)}W")
        print(f"Min Power: {min(power_values)}W")
    else:
        print(f"No data found for device ID: {device_id}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python query_device.py <device_id>")
    else:
        query_device(sys.argv[1])
