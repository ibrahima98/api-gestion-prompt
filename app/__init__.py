from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import Config
from app.db import init_app
from app.models.admin.auth_admin import auth_bp
from app.views.users.users_views import user_bp
from app.views.prompt.prompt_views import prompt_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    JWTManager(app)  # Initialisez JWTManager avec votre application Flask

    init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(prompt_bp, url_prefix='/prompt')


    return app
