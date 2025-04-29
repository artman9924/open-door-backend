from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS

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
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/post-message', methods=['POST'])
def post_message():
    data = request.get_json()
    message = data.get('message', '')

    print(f"Received message: {message}")  # Print to confirm backend is receiving

    if not message:
        return jsonify({'error': 'No message provided.'}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO messages (content) VALUES (?)', (message,))
    conn.commit()
    conn.close()

    return jsonify({'status': 'Message saved successfully!'})

@app.route('/get-messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM messages ORDER BY timestamp DESC').fetchall()
    conn.close()

    return jsonify([dict(msg) for msg in messages])

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
