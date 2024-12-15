import time
import hashlib
import requests
from datetime import datetime, timezone

ping_pong_service_url = "http://pingpong-service.pingpong-log.svc.cluster.local:3000/getpong"
reader_service_url = "http://log-output-svc:3002/update"

def compute_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

while True:
    try:
        # Fetch ping-pong count from Ping-pong service
        response = requests.get(ping_pong_service_url)
        response.raise_for_status()
        ping_pong_data = response.json()
        ping_pong_count = ping_pong_data.get("count", 0)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching pong count: {e}")
        ping_pong_count = 0

    # Generate timestamp and hash
    timestamp = datetime.now(timezone.utc).isoformat()
    data = {
        "timestamp": timestamp,
        "hash": compute_hash(timestamp),
        "ping_pongs": ping_pong_count
    }

    try:
        # Send the data to the Reader
        post_response = requests.post(reader_service_url, json=data)
        post_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to Reader: {e}")

    time.sleep(5)
