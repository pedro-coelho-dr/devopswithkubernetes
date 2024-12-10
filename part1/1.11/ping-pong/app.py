import os
import json
from flask import Flask, jsonify

app = Flask(__name__)

file_path = "/usr/src/app/data/requests.json"


os.makedirs(os.path.dirname(file_path), exist_ok=True)

if os.path.exists(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
        count = data.get("count", 0)
else:
    count = 0

@app.route("/pingpong", methods=["GET"])
def ping_pong():
    global count
    count += 1

    with open(file_path, "w") as f:
        json.dump({"count": count}, f)

    return jsonify({"response": f"pong {count}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
