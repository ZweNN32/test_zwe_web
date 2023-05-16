from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('templates/login.html')

@auth.route('/logout')
def logout():
    return render_template('templates/logout.html')

@auth.route('/signup')
def signup():
    return render_template('templates/signup.html')


