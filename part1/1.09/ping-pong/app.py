from flask import Flask, jsonify

app = Flask(__name__)

counter = {"count": 0}

@app.route("/pingpong", methods=["GET"])
def ping_pong():
    counter["count"] += 1
    return jsonify({"response": f"pong {counter['count']}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
