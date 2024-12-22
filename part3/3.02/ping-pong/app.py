from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST", "postgres-service")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

if not all([DB_USER, DB_PASSWORD, DB_NAME]):
    raise RuntimeError("Database credentials are not fully set in environment variables.")

def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME, 
        user=DB_USER, 
        password=DB_PASSWORD, 
        host=DB_HOST, 
        port=DB_PORT
    )

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS counter (
            id SERIAL PRIMARY KEY,
            count INTEGER NOT NULL
        )
    """)
    cur.execute("""
        INSERT INTO counter (count)
        SELECT 0
        WHERE NOT EXISTS (SELECT 1 FROM counter)
    """)
    conn.commit()
    cur.close()
    conn.close()

init_db()

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Welcome to Ping-Pong Service"})


@app.route("/pingpong", methods=["GET"])
def ping_pong():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE counter SET count = count + 1 RETURNING count")
    new_count = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"response": f"pong {new_count}"})

@app.route("/getpong", methods=["GET"])
def get_count():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT count FROM counter")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({"count": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
