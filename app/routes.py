from app import app
from flask import render_template, url_for

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', title='Home')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')
