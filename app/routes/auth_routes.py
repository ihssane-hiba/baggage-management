from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.services.user_service import UserService
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    print('Login here' )
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f'username = {username} password = {password}')
        user = UserService.get_user_by_username(username)
        print(f'Login successful of user {user.username} and password {password}')
        
        
        # check_password_hash is a methode that returns if the hashed password stored in the database is correct to the password the user given 
        # it is not the same as the password stored in the database
        # thats why i used simple check
        # you can use check_password_hash if you stord the password with set_password_hash
        # that way you password stored in the database will hashed so we can compare it to the password given by the user
        
        if user.password == password: #user and check_password_hash(user.password, password):
            session['logged_in'] = True
            session['username'] = user.username
            session['role'] = user.role
            flash('Login successful!', 'success')
            print ('Login successful asdfasdfasd')
            return redirect(url_for('parcel.list_parcels'))
        else:
            flash('Invalid credentials.', 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    print('user logged out successfully')
    return redirect(url_for('auth.login'))
