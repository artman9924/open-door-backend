from flask import Blueprint, request, jsonify
from db import get_db_connection
from analysis import analyze_emotion, MODERATION_KEYWORDS

main_routes = Blueprint("main", __name__)

@main_routes.route("/get-messages", methods=["GET"])
def get_messages():
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM messages ORDER BY timestamp DESC').fetchall()
    conn.close()
    return jsonify([dict(msg) for msg in messages])

@main_routes.route("/post-message", methods=["POST"])
def post_message():
    data = request.get_json()
    message = data.get("content", "").strip()
    mood = data.get("mood", None)

    if not message:
        return jsonify({"error": "No message provided."}), 400

    emotion = analyze_emotion(message)
    flagged = any(word in message.lower() for word in MODERATION_KEYWORDS)

    try:
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO messages (content, flagged, emotion_tag, mood) VALUES (?, ?, ?, ?)",
            (message, int(flagged), emotion, mood)
        )
        conn.commit()
        conn.close()
        return jsonify({"status": "Message saved successfully!", "flagged": flagged})
    except Exception:
        return jsonify({"error": "Server error occurred"}), 500
