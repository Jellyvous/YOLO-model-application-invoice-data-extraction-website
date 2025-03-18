import os
from werkzeug.utils import secure_filename
from flask import request, jsonify
import json
from app.config import Config
from app.services.image_processing_service import ImageProcessingService

class ProcessController:
    def __init__(self):
        self.image_processor = ImageProcessingService()
        
    def process_invoice(self):
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400
        
        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({"error": "No selected image file"}), 400
        
        filename = secure_filename(request.files.filename)
        filepath = os.path.join(Config['UPLOAD_FOLDER'], filename)
        request.files.save(filepath)

        # Process image
        result_json_path, processed_image_path, extracted_text = ImageProcessingService.process_image(filepath, filename)
        
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
            'extracted_text': extracted_text
        }

        return jsonify(response_data)