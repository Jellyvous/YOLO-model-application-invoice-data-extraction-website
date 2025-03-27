# app/controllers/main_controller.py
import os
from werkzeug.utils import secure_filename
from app.config import Config
from flask import render_template, request, redirect, url_for, session, json, jsonify
from app.controllers.process_controller import ProcessController
from app.services.image_processing_service import ImageProcessingService
from app.services.save_invoice import save_invoice



class HomeController:
    def __init__(self):
        self.image_processor = ImageProcessingService()

    
    def index(self):
        if 'username' not in session:
            return redirect(url_for('auth.login_user'))

        if request.method == 'POST':
            if 'file' in request.files:
                                    
                image_file = request.files['file']
                if image_file.filename == '':
                    return jsonify({"error": "No selected image file"}), 400
            
                filename = secure_filename(image_file.filename)
                filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
                image_file.save(filepath)

                # Process image
                result_json_path, processed_image_path, extracted_text = self.image_processor.process_image(filepath, filename)
            
                # Read data
                with open(result_json_path, 'r', encoding='utf-8') as f:
                    result_data = json.load(f)

                store_name = None
                items = []
                
                for item in result_data.get("R.jpg", []):
                    store_name = item.get("store_name", "")
                    for sub_item in item.get("items", []):
                        if "item" in sub_item and "quantity" in sub_item:
                            items.append({
                                "item": sub_item.get("item", ""),
                                "quantity": sub_item.get("quantity", ""),
                                "price": sub_item.get("price", "")
                        })

                response_data = {
                    'result_data': items,
                    'store_name': store_name,
                    'extracted_text': extracted_text if extracted_text else ""
                }
                return jsonify(response_data)

                
            elif request.is_json:
                json_data = request.get_json() 
                save_invoice(json_data)
                return jsonify({'message': 'JSON data received successfully'}), 200

            
            else:
                return jsonify({'error': 'Invalid file type'}), 400
        return render_template('index.html')

        
