from app import app
from flask import render_template, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/home')
def index():
    user = {'username': 'Miguel'}
    return render_template('home.html', title='Home', user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
