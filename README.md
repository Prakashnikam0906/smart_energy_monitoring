
# Smart Energy Monitoring System

## Project Objective
To build a simulated smart embedded system that:
- Monitors energy usage of 3 appliances
- Stores data locally
- Sends data to a cloud server
- Visualizes real-time energy statistics

## Overview
This project simulates a **Smart Home Energy Monitoring System** using:
- **Python** for embedded-like simulation of sensors
- **Flask** as a cloud server to visualize data
- **MQTT** (simulated) for communication
- **Local file storage** for data logging

No physical hardware (like ESP32 or sensors) is used — all readings are randomly generated to mimic real-world conditions.

##  System Components
- `embedded/`: Simulates sensor readings and device-level logic
- `server/`: Flask web app to receive and visualize energy data
- `data/`: Stores local logs and communication history
- `docs/`: Project documentation and diagrams
- `demo/`: Optional folder for screen recordings


## Simulated Workflow
1. Sensor values (energy usage) generated randomly
2. Values logged locally to `sensor_log.csv`
3. Data "published" via simulated MQTT
4. Flask server receives data and updates live dashboard

## Features
- Per-appliance energy monitoring
- Local and cloud data storage
- Real-time dashboard
- Modular Python scripts

## 🛠️ How to Run
1. Start Flask server:
   ```bash
   cd server
   python server.py
