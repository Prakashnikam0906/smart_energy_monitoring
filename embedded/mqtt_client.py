# embedded/mqtt_client.py

import requests
from utils import log_error

# Updated endpoint to match Flask server
SERVER_URL = "http://192.168.9.86:5000/energy"

def send_to_server(data):
    try:
        response = requests.post(SERVER_URL, json=data, timeout=3)
        if response.status_code != 200:
            log_error(f"Server responded with status {response.status_code}: {response.text}")
    except requests.exceptions.Timeout:
        log_error("Timeout: Server did not respond.")
    except requests.exceptions.ConnectionError:
        log_error("ConnectionError: Could not reach server.")
    except Exception as e:
        log_error(f"Send Error: {str(e)}")
