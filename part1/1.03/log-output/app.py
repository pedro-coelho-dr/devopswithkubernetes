import time
import uuid
from datetime import datetime, timezone


random_string = str(uuid.uuid4())

print(f"Application started with ID: {random_string}")

while True:
    timestamp = datetime.now(timezone.utc).isoformat()
    print(f"{timestamp}: {random_string}")
    time.sleep(5)
