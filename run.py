import os
from flask import Flask
from dotenv import load_dotenv
from app.routes import home_routes
from app.config import Config

# Load environment variables
load_dotenv()
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
RESULT_FOLDER = os.getenv('RESULT_FOLDER')
SECRET_KEY = os.getenv('SECRET_KEY')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = app.config['SECRET_KEY']

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)
    
    home_routes.register_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
