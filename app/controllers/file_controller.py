from flask import send_from_directory
from app.config import Config

class FileController:
    def __init__(self):
        pass
        
    def download_file(self, filename):
        return send_from_directory(Config['RESULT_FOLDER'], filename, as_attachment=True)