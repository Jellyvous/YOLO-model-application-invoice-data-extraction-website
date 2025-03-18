from werkzeug.utils import secure_filename
from app.services.process_image import process_image
from flask import jsonify
import json
import os
from app.config import UPLOAD_FOLDER, RESULT_FOLDER

def process_uploaded_file(file):
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Process image
    result_json_path, processed_image_path, extracted_text = process_image(filepath, filename)
    
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

