from flask import Blueprint, jsonify, request

backend_routes = Blueprint("backend_routes", __name__)

todos = []  # In-memory store for todos

@backend_routes.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos), 200

@backend_routes.route("/todos", methods=["POST"])
def add_todo():
    todo = request.json.get("todo")
    if not todo:
        return jsonify({"error": "Todo is required"}), 400
    if len(todo) > 140:
        return jsonify({"error": "Todo must not exceed 140 characters"}), 400
    if not todo.strip():
        return jsonify({"error": "Todo cannot be empty or whitespace-only"}), 400
    todos.append(todo)
    return jsonify({"message": "Todo added"}), 201
