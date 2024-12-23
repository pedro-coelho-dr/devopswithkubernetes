import requests
from flask import render_template, send_from_directory, request, jsonify
from .services.image_service import get_cached_image


BACKEND_URL = "http://todo-backend-service:5001/todos"

def init_routes(app):
    @app.route("/")
    def todo():
        image_path = get_cached_image()

## GET_TODO
        try:
            response = requests.get(BACKEND_URL)
            response.raise_for_status()
            todos = response.json()
        except requests.RequestException as e:
            print(f"Error fetching TODOs: {e}")
            todos = []

        return render_template("index.html", image_path="image.jpg", todos=todos)

    @app.route("/image.jpg")
    def serve_image():
        return send_from_directory("/usr/src/app/data", "image.jpg")


## ADD_TODO
    @app.route("/add-todo", methods=["POST"])
    def add_todo():
        todo = request.form.get("todo", "").strip()

        if not todo:
            return jsonify({"error": "Todo cannot be empty"}), 400

        try:
            response = requests.post(BACKEND_URL, json={"todo": todo})
            response.raise_for_status()
            return jsonify({"message": "Todo added"}), 201
        except requests.RequestException as e:
            print(f"Error adding TODO: {e}")
            return jsonify({"error": "Failed to add TODO"}), 500
