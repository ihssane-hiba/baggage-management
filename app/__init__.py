from flask import Flask
from app.utils.db_setup import setup_database
from app.routes import auth_routes, user_routes, parcel_routes, index_routes
from config import Config


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Setup database
    setup_database(app)

    # Register blueprints (routes)
    app.register_blueprint(index_routes.index_bp)
    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(user_routes.user_bp)
    app.register_blueprint(parcel_routes.parcel_bp)

    return app
