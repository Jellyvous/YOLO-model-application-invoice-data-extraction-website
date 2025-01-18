from flask import Flask, render_template, request, send_file, session, send_from_directory, jsonify, url_for, redirect
from werkzeug.utils import secure_filename
import os
from utils.process_image import process_image
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import bcrypt
from config import UPLOAD_FOLDER, RESULT_FOLDER

app = Flask(__name__)
app.secret_key = os.urandom(24)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

uri = "mongodb+srv://root:root@cluster0.eqptv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(uri, server_api=ServerApi('1'))
db = client["yolo"]
users_collection = db["user"]


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
    



@app.route('/login', methods=['POST', 'GET'])
def login():
    
    if request.method == 'POST':
        existing_user = users_collection.find_one({'username' : request.form['username']})
        
        if existing_user is None:
            return 'Username does not exists'
        
        if bcrypt.checkpw(request.form['password'].encode('utf-8'), existing_user['password']):
            session['username'] = request.form['username']  
            return redirect(url_for('index'))
        else:
            return 'Invalid password'

    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':

        existing_user = users_collection.find_one({'username' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users_collection.insert_one({'username': request.form['username'], 'email': request.form['email'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'That username is already exists'

    return render_template('register.html')

@app.route('/', methods=['POST', 'GET'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))


    
    if request.method == 'POST':
        if 'file' in request.files:
            f = request.files['file']
            filename = secure_filename(f.filename)
            filepath = os.path.join(UPLOAD_FOLDER, f.filename)
            f.save(filepath)

            result_json_path, processed_image_path, extracted_text = process_image(filepath, filename)

            return jsonify({'extracted_text': extracted_text})
        else:
            return jsonify({'error': 'Invalid file type'}), 400

    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(RESULT_FOLDER, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
