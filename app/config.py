import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(os.path.dirname(basedir), '.env'))

class Config:
    """Base configuration class"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads/')
    RESULT_FOLDER = os.getenv('RESULT_FOLDER', 'results/')

    # MongoDB URI
    MONGO_URI = os.getenv('MONGO_URI')

    # Secret key for sessions
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Model path
    MODELS_FOLDER = os.path.join(BASE_DIR, 'app', 'ml_models', 'yolo', 'weights')
