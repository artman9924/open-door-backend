from flask import Blueprint, request, redirect
from db import get_db_connection
import os

admin_routes = Blueprint("admin", __name__)
ADMIN_KEY = os.getenv("ADMIN_KEY")

@admin_routes.route("/admin")
def admin_panel():
    key = request.args.get("key")
    if key != ADMIN_KEY:
        return "Unauthorized", 403

    conn = get_db_connection()
    messages = conn.execute("SELECT * FROM messages ORDER BY timestamp DESC").fetchall()
    conn.close()

    html = "<h1>Open Door Admin Panel</h1><ul>"

    if not messages:
        html += "<p>No messages to show.</p>"
    else:
        html += "<ul>"

    for index, msg in enumerate(messages):
        flagged = int(msg['flagged']) if msg['flagged'] else 0
        flagged_badge = '<span style="color:red;font-weight:bold;">[FLAGGED]</span>' if flagged else ''
        newest = "<strong>[Newest]</strong> " if index == 0 else ""
        html += f"""
        <li>
            {flagged_badge} {newest}#{msg['id']} — {msg['content']} [{msg['emotion_tag'] or ''}]
            <em>({msg['timestamp']})</em>
            <form method="POST" action="/delete-message/{msg['id']}?key={key}" style="display:inline;">
                <button type="submit">Delete</button>
            </form>
        </li>
        """

    html += "</ul>"
    return html

@admin_routes.route("/delete-message/<int:msg_id>", methods=["POST"])
def delete_message(msg_id):
    key = request.args.get("key")
    if key != ADMIN_KEY:
        return "Unauthorized", 403

    conn = get_db_connection()
    conn.execute("DELETE FROM messages WHERE id = ?", (msg_id,))
    conn.commit()
    conn.close()

    return redirect(f"/admin?key={key}")
