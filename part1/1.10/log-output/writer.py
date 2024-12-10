import time
import json
import hashlib
from datetime import datetime, timezone

file_path = "/usr/src/app/data/data.json"

def compute_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

while True:
    timestamp = datetime.now(timezone.utc).isoformat()
    data = {
        "timestamp": timestamp,
        "hash": compute_hash(timestamp)
    }
    with open(file_path, "w") as f:
        json.dump(data, f)
    time.sleep(5)
