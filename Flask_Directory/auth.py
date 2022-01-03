from flask import render_template, request, redirect, flash, url_for
from Flask_Directory import app
from .models import *
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required

'''ADMIN login/authentication, logout, and post capabilities'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email-login')
        password = request.form.get('password-login')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Login successful.', category='success')
                login_user(user, remember=True)
                return redirect(url_for('post'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html')

@app.route('/post')
@login_required
def post():
    return render_template('post.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
