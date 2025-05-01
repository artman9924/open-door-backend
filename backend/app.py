from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from dotenv import load_dotenv
from textblob import TextBlob
load_dotenv()
import sqlite3
import os

app = Flask(__name__)
CORS(app)

def analyze_emotion(message):
    polarity = TextBlob(message).sentiment.polarity
    if polarity > 0.4:
        return "hopeful"
    elif polarity > 0.1:
        return "relieved"
    elif polarity < -0.4:
        return "angry"
    elif polarity < -0.1:
        return "sad"
    else:
        return "neutral"

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
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            flagged INTEGER DEFAULT 0,
            emotion_tag TEXT
        );
    ''')
    conn.commit()
    conn.close()
    
# Initialize DB if it doesn't exist
if not os.path.exists('database.db'):
    print("Database not found. Initializing database...")
    init_db()
else:
    print("Database already exists.")

def add_flagged_column():
    conn = get_db_connection()
    try:
        conn.execute('ALTER TABLE messages ADD COLUMN flagged INTEGER DEFAULT 0')
        print("Added 'flagged' column to messages table.")
    except sqlite3.OperationalError:
        print("'flagged' column already exists.")
    conn.commit()
    conn.close()

# Ensure database is initialized on first import
if not os.path.exists('database.db'):
    print("Database not found. Initializing database...")
    init_db()
    add_flagged_column()
else:
    print("Database already exists.")
    add_flagged_column()


@app.route('/get-messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM messages ORDER BY timestamp DESC').fetchall()
    conn.close()
    return jsonify([dict(msg) for msg in messages])

MODERATION_KEYWORDS = ['suicide', 'kill', 'abuse', 'hate', 'die', 'harm']

@app.route('/post-message', methods=['POST'])
def post_message():
    data = request.get_json()
    message = data.get('content', '').strip()
    emotion = analyze_emotion(message)

    if not message:
        return jsonify({'error': 'No message provided.'}), 400

    # ✅ Define flagged only if message is valid
    flagged = any(word in message.lower() for word in MODERATION_KEYWORDS)

    try:
        conn = get_db_connection()
        conn.execute('INSERT INTO messages (content, flagged) VALUES (?, ?, ?)', (message, int(flagged), emotion))
        conn.commit()
        conn.close()

        print(f"Message received: '{message}' | Flagged: {flagged}") 

        return jsonify({'status': 'Message saved successfully!', 'flagged': flagged})
    except Exception as e:
        print("Error in post_message:", str(e))
        return jsonify({'error': 'Server error occurred'}), 500


ADMIN_KEY = os.getenv("ADMIN_KEY")

@app.route('/admin')
def admin_panel():
    key = request.args.get('key')
    if key != ADMIN_KEY:
        return "Unauthorized", 403

    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM messages ORDER BY timestamp DESC').fetchall()
    conn.close()

    html = "<h1>Open Door Admin Panel</h1><ul>"

    if not messages:
        html += "<p>No messages to show.</p>"
    else:
        html += "<ul>"
    for msg in messages:
        flagged = int(msg['flagged']) if msg['flagged'] is not None else 0
        flagged_style = "color: red; font-weight: bold;" if flagged == 1 else ""
        
        # Conditionally show the "FLAGGED" badge
        flagged_badge = (
            '<span style="background: #fdd; color: #900; padding: 2px 6px; border-radius: 6px; margin-right: 8px;">FLAGGED</span>'
            if flagged == 1 else ''
        )
        
        emotion_display = f"<span style='color: #888; font-size: 0.9em;'> [{msg['emotion_tag']}]</span>" if msg['emotion_tag'] else ""

        html += f"""
        <li>
            {flagged_badge}
            <span style="{flagged_style}"><strong>#{msg['id']}</strong> — {msg['content']}</span>
            {emotion_display}
            <em>({msg['timestamp']})</em>
            <form method="POST" action="/delete-message/{msg['id']}?key={key}" style="display:inline;">
                <button type="submit">Delete</button>
            </form>
        </li>
        """

        html += "</ul>"

    return html

@app.route('/delete-message/<int:msg_id>', methods=['POST'])
def delete_message(msg_id):
    key = request.args.get('key')
    if key != ADMIN_KEY:
        return "Unauthorized", 403

    conn = get_db_connection()
    conn.execute('DELETE FROM messages WHERE id = ?', (msg_id,))
    conn.commit()
    conn.close()

    return redirect(f"/admin?key={key}")
