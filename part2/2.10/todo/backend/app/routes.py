from flask import Blueprint, jsonify, request
import psycopg2
import os

backend_routes = Blueprint("backend_routes", __name__)

# Establish database connection
DB_HOST = os.getenv("POSTGRES_HOST", "todo-db-service")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@backend_routes.route("/todos", methods=["GET"])
def get_todos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM todos")
    todos = [{"id": row[0], "content": row[1]} for row in cursor.fetchall()]
    cursor.close()
    conn.close()
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

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (content) VALUES (%s) RETURNING id", (todo,))
    todo_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"id": todo_id, "message": "Todo added"}), 201

