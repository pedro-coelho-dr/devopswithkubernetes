import os
import time
import json
import hashlib
from datetime import datetime, timezone

file_path = "/usr/src/app/data/data.json"
ping_pong_file = "/usr/src/app/data/requests.json"  # Ping-pong count file

def compute_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

while True:
    # Read the ping-pong count from requests.json
    if os.path.exists(ping_pong_file):
        with open(ping_pong_file, "r") as f:
            ping_pong_data = json.load(f)
        ping_pong_count = ping_pong_data.get("count", 0)
    else:
        ping_pong_count = 0

    # Generate timestamp and hash
    timestamp = datetime.now(timezone.utc).isoformat()
    data = {
        "timestamp": timestamp,
        "hash": compute_hash(timestamp),
        "ping_pongs": ping_pong_count
    }

    # Write the data to data.json
    with open(file_path, "w") as f:
        json.dump(data, f)
    time.sleep(5)
