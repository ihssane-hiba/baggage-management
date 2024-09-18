from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def list_users():
    users = UserService.get_all_users()
    return render_template('list_users.html', users=users)
