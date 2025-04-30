from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()
    conn.close()

# Ensure database is initialized on first import
if not os.path.exists('database.db'):
    print("Database not found. Initializing database...")
    init_db()
else:
    print("Database already exists.")

@app.route('/get-messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM messages ORDER BY timestamp DESC').fetchall()
    conn.close()
    return jsonify([dict(msg) for msg in messages])

@app.route('/post-message', methods=['POST'])
def post_message():
    data = request.get_json()
    message = data.get('content', '')

    print(f"Received message: {message}") # Log to Render

    if not message:
        return jsonify({'error': 'No message provided.'}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO messages (content) VALUES (?)', (message,))
    conn.commit()
    conn.close()

    return jsonify({'status': 'Message saved successfully!'})

