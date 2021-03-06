from flask import render_template, request, redirect, flash, url_for
from Flask_Directory import app
from .models import *
from . import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required
from .forms import CreatePost

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


@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = CreatePost()

    if request.method == 'POST':
        title = form.title.data
        slug = form.slug.data
        content = form.content.data

        blog_post = Post(title=title, slug=slug, content=content)
        db.session.add(blog_post)
        db.session.commit()

        return redirect(url_for('blog'))

    return render_template('post.html', form=form)


@app.route('/delete-post/<int:id>')
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('index'))
