from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.services.user_service import UserService
from werkzeug.security import check_password_hash

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/', methods=['GET', 'POST'])
def login():
    print('Login here' )
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f'username = {username} password = {password}')
        user = UserService.get_user_by_username(username)
        print('Login successful of user %s' % user)
        if user and check_password_hash(user.password, password):
            session['logged_in'] = True
            session['username'] = user.username
            session['role'] = user.role
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials.', 'danger')
    return render_template('login.html')

@auth_routes.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    print('user logged out successfully')
    return redirect(url_for('auth.login'))
