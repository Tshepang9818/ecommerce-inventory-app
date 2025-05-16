# config.py
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Use SQLite for simplicity here
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'inventory.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
