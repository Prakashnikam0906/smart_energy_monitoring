# server/server.py

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests (optional)

# In-memory data store
energy_data = []

# Root route for status check
@app.route("/", methods=["GET"])
def home():
    return " Smart Energy Monitoring Server is running. Visit /dashboard to view data."

# POST endpoint for receiving energy usage data
@app.route("/energy", methods=["POST"])
def receive_energy_data():
    try:
        data = request.get_json()
        data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        energy_data.append(data)
        print(f"Received: {data}")
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Dashboard to show energy statistics
@app.route("/dashboard", methods=["GET"])
def dashboard():
    if not energy_data:
        return "⚠️ No data received yet."

    stats = {}
    for item in energy_data:
        device = item["device_id"]
        power = item["power"]

        if device not in stats:
            stats[device] = {
                "readings": [],
                "avg": 0,
                "max": power,
                "min": power,
            }

        stats[device]["readings"].append(power)
        stats[device]["max"] = max(stats[device]["max"], power)
        stats[device]["min"] = min(stats[device]["min"], power)

    for device in stats:
        readings = stats[device]["readings"]
        stats[device]["avg"] = round(sum(readings) / len(readings), 2)

    return render_template("dashboard.html", data=stats)

if __name__ == "__main__":
    os.environ["FLASK_ENV"] = "development"
    app.run(host="0.0.0.0", port=5000)
