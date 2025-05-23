from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

from routes.admin import admin_routes
from routes.main import register_main_routes

limiter = Limiter(
    get_remote_address,
    app=app,
    # default_limits=["1 per 30 seconds"]
)

# Register routes
# app.register_blueprint(register_main_routes)
app.register_blueprint(admin_routes)
register_main_routes(app, limiter)

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

