from flask import render_template, request, redirect, url_for, session, flash, jsonify
from pymongo import MongoClient
from app.config import Config
import datetime

# MongoDB connection
client = MongoClient(Config.MONGO_URI)
db = client["yolo"]
users_collection = db["user"]
invoices_collection = db["data-invoice"] 

import datetime
from flask import session

def save_invoice(invoice_data):
    try:
        username = session.get('username')

        if not username:
            return {'error': 'User not logged in'}, 401  
        existing_user = users_collection.find_one({'username': username})
        
        if not existing_user:
            return {'error': 'User not found'}, 404  
        client_id = existing_user.get('_id')  

        invoice_data["client_id"] = str(client_id)  
        current_time = datetime.datetime.now()
        invoice_data["timestamp"] = current_time

        invoices_collection.insert_one(invoice_data)

        return {'message': 'Invoice data saved successfully!'}, 200

    except Exception as e:
        print(f"Error saving invoice data: {e}")
        return {'error': 'Failed to save invoice data'}, 500
