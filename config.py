import os

# Paths
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads/')
RESULT_FOLDER = os.getenv('RESULT_FOLDER', 'results/')

# MongoDB URI
MONGO_URI = os.getenv('MONGO_URI')

# Secret key for sessions
SECRET_KEY = os.getenv('SECRET_KEY')
