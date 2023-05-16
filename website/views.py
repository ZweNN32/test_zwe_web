from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/writer')
def writer():
    return render_template('writer.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/stranger')
def stranger():
    return render_template('stranger.html')

@views.route('/oamirror')
def oamirror():
    return render_template('oamirror.html')

@views.route('/alive')
def alive():
    return render_template('alive.html')
 
@views.route('/iponder')
def iponder():
    return render_template('iponder.html')

@views.route('/whowht')
def whowht():
    return render_template('whowht.html')

@views.route('/zwe')
def zwe():
    return render_template('zwe.html')