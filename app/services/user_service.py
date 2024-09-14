from app.models.user import User
from app.utils.db_setup import db

class UserService:
    @staticmethod
    def create_user(username, password, role):
        new_user = User(username=username, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
