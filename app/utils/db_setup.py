from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI']
    db.init_app(app)

    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
