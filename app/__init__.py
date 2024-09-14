from flask import Flask
from app.utils.db_setup import setup_database
from app.routes import auth_routes, user_routes, parcel_routes

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Setup database
    setup_database(app)

    # Register blueprints (routes)
    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(user_routes.user_bp)
    app.register_blueprint(parcel_routes.parcel_bp)

    return app
