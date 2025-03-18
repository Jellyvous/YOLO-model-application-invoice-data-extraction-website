# app/controllers/auth_controller.py
from flask import render_template, request, redirect, url_for, session, flash
import bcrypt
from app.database import users_collection

class AuthController:
    @staticmethod
    def login_user():
        if request.method == 'POST':
            existing_user = users_collection.find_one({'username': request.form['username']})
            if existing_user is None:
                flash('Username does not exist!', 'error')  
                return redirect(url_for('auth.login_user'))  
                   
            if existing_user is None or not bcrypt.checkpw(request.form['password'].encode('utf-8'), existing_user['password']):
                flash('Wrong username or password!', 'error')  
                return redirect(url_for('auth.login_user')) 
           
            session['username'] = request.form['username']
            return redirect(url_for('home.index'))
        return render_template('login.html')

    @staticmethod
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
                return redirect(url_for('home.index'))
            flash('Username already exist!', 'error')  
            return redirect(url_for('auth.register_user')) 
        return render_template('register.html')

    @staticmethod
    def logout_user():
        session.pop('username', None)
        return redirect(url_for('auth.login_user'))