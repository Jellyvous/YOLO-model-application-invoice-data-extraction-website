from werkzeug.utils import secure_filename
from utils.process_image import process_image
from flask import jsonify
import os
from config import UPLOAD_FOLDER, RESULT_FOLDER

def process_uploaded_file(file):
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Process image
    result_json_path, processed_image_path, extracted_text = process_image(filepath, filename)

    return jsonify({'extracted_text': extracted_text})
