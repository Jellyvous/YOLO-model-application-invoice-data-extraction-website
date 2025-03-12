from flask import render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
import bcrypt
from config import MONGO_URI

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client["yolo"]
users_collection = db["user"]

def login_user():
    if request.method == 'POST':
        existing_user = users_collection.find_one({'username': request.form['username']})
        if existing_user is None:
            flash('Username does not exist!', 'error')  
            return redirect(url_for('login'))  
               
        if existing_user is None or not bcrypt.checkpw(request.form['password'].encode('utf-8'), existing_user['password']):
            flash('Wrong username or password!', 'error')  
            return redirect(url_for('login')) 
       
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

def register_user():
    if request.method == 'POST':
        existing_user = users_collection.find_one({'username': request.form['username']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users_collection.insert_one({
                'username': request.form['username'], 
                'email': request.form['email'], 
                'password': hashpass
            })
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        flash('Username already exist!', 'error')  
        return redirect(url_for('register')) 
    return render_template('register.html')
