import json
import hashlib
from flask import Flask, jsonify, request

app = Flask(__name__)
log_data = {}

def compute_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

@app.route("/update", methods=["POST"])
def update_data():
    global log_data
    try:
        # Receive data from Writer
        log_data = request.json
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/log")
def display_data():
    try:
        # Extract data for display
        timestamp = log_data.get("timestamp", "No timestamp found")
        ping_pongs = log_data.get("ping_pongs", 0)
        generated_hash = compute_hash(timestamp)
        stored_hash = log_data.get("hash", "No hash found")

        # Verify the hash
        if generated_hash == stored_hash:
            response = {
                "timestamp": timestamp,
                "hash": stored_hash,
                "ping_pongs": ping_pongs,
                "status": "verified"
            }
        else:
            response = {
                "timestamp": timestamp,
                "stored_hash": stored_hash,
                "generated_hash": generated_hash,
                "ping_pongs": ping_pongs,
                "status": "hash mismatch"
            }
        return jsonify(response)
    except KeyError:
        return jsonify({"error": "Invalid data in memory."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002)
