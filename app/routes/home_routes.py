from flask import Blueprint
from app.controllers.process_controller import ProcessController
from app.controllers.home_controller import HomeController
from app.controllers.file_controller import FileController
from app.controllers.auth_controller import AuthController



def register_routes(app):
    process_controller = ProcessController()
    home_controller = HomeController()
    file_controller = FileController()
    
    process_bp = Blueprint('process', __name__)
    home_bp = Blueprint('home', __name__)
    auth_bp = Blueprint('auth', __name__)

    
    process_bp.route('/process', methods=['POST'])(process_controller.process_invoice)
    home_bp.route('/', methods=['GET', 'POST'])(home_controller.index)
    home_bp.route('/download/<filename>', methods=['GET'])(lambda filename: file_controller.download_file(filename))
    
    auth_bp.route('/login', methods=['GET', 'POST'])(AuthController.login_user)
    auth_bp.route('/register', methods=['GET', 'POST'])(AuthController.register_user)
    auth_bp.route('/logout')(AuthController.logout_user)

    app.register_blueprint(process_bp, url_prefix='/api')
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
