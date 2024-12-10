import json
import hashlib
from flask import Flask, jsonify

app = Flask(__name__)
file_path = "/usr/src/app/data/data.json"

def compute_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

@app.route("/log")
def display_data():
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        timestamp = data.get("timestamp", "No timestamp found")
        generated_hash = compute_hash(timestamp)
        stored_hash = data.get("hash", "No hash found")

        # Verify the hash
        if generated_hash == stored_hash:
            response = {
                "timestamp": timestamp,
                "hash": stored_hash,
                "status": "verified"
            }
        else:
            response = {
                "timestamp": timestamp,
                "stored_hash": stored_hash,
                "generated_hash": generated_hash,
                "status": "hash mismatch"
            }
        return jsonify(response)
    except FileNotFoundError:
        return jsonify({"error": "JSON file not found. Writer may not have started yet."}), 404
    except KeyError:
        return jsonify({"error": "Invalid data in JSON file."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
