from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    user = {'username': 'Miguel'}
    return render_template('home.html', title='Home', user=user)

<<<<<<< HEAD
@app.route('/log', methods=['GET', 'POST'])
=======
@app.route('/login', methods=['GET', 'POST'])
>>>>>>> 2a05bcc6eb525b2758a6ce802e26e75b00b989f5
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)
