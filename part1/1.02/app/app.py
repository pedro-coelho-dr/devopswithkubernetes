import os
from flask import Flask


port = int(os.getenv("PORT", 5000))
app = Flask(__name__)

@app.route("/")
def home():
    return "TODO Application"

if __name__ == "__main__":
    print(f"Server started in port {port}")
    app.run(host="0.0.0.0", port=port)
