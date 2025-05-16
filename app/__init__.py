# app/__init__.py
from flask import Flask
from app.database import db
from app.routes import inventory_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Register blueprints (API endpoints)
    app.register_blueprint(inventory_bp)

    return app
