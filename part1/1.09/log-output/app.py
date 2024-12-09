import uuid
from datetime import datetime, timezone
from flask import Flask, jsonify

random_string = str(uuid.uuid4())
print(f"Application started with ID: {random_string}")

app = Flask(__name__)


status = {"random_string": random_string, "timestamp": None}

@app.route("/log", methods=["GET"])
def get_status():
    status["timestamp"] = datetime.now(timezone.utc).isoformat()
    return jsonify(status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
