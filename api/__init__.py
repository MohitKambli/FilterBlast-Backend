from flask import Flask
from flask_cors import CORS
from .routes import main, image_routes, log_routes
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, origins=["http://localhost:3000", "https://musical-lokum-0e48e8.netlify.app"])

    # Register blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(image_routes.bp)
    app.register_blueprint(log_routes.bp)

    return app
