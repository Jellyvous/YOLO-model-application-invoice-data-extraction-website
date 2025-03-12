from flask import Flask, render_template, request, send_from_directory, session, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os
from services.auth import login_user, register_user
from services.image_processing import process_uploaded_file
from config import UPLOAD_FOLDER, RESULT_FOLDER

app = Flask(__name__)

# Load environment variables
load_dotenv()
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
RESULT_FOLDER = os.getenv('RESULT_FOLDER')
SECRET_KEY = os.getenv('SECRET_KEY')

app.secret_key = SECRET_KEY

@app.route('/login', methods=['POST', 'GET'])
def login():
    return login_user()

@app.route('/register', methods=['POST', 'GET'])
def register():
    return register_user()

@app.route('/', methods=['POST', 'GET'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'file' in request.files:
            return process_uploaded_file(request.files['file'])
        else:
            return jsonify({'error': 'Invalid file type'}), 400

    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(RESULT_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
