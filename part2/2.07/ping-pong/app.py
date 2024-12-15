from flask import Flask, jsonify

app = Flask(__name__)

# Counter stored in memory
counter = {"count": 0}

@app.route("/pingpong", methods=["GET"])
def ping_pong():
    counter["count"] += 1
    return jsonify({"response": f"pong {counter['count']}"})

@app.route("/getpong", methods=["GET"])
def get_count():
    return jsonify({"count": counter["count"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)