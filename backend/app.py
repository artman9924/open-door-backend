from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from routes.main import main_routes
from routes.admin import admin_routes

load_dotenv()

app = Flask(__name__)
CORS(app)

# Register routes
app.register_blueprint(main_routes)
app.register_blueprint(admin_routes)

if __name__ == "__main__":
    from db import init_db, add_flagged_column

    if not os.path.exists("database.db"):
        print("Database not found. Initializing...")
        init_db()
        add_flagged_column()
    else:
        print("Database already exists.")
        add_flagged_column()

    app.run(debug=True)
