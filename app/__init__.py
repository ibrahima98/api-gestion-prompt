from flask import Flask
from app.config import Config
from .db import init_app
from .views.admin_views import bp as admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_app(app)

    app.register_blueprint(admin_bp)

    return app
