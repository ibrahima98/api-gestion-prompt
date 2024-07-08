from flask import Flask
from app.config import Config
from .db import init_app
from app.views.admin.admin_views import bp as admin_bp
from app.models.admin.auth_admin import auth_bp
from flask_jwt_extended import JWTManager
from app.views.users.users_views import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_app(app)

    JWTManager(app)

    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')  #Enregistrement du blueprint auth
    app.register_blueprint(user_bp, url_prefix='/user')

    return app