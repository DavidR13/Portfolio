from flask import render_template
from Flask_Directory import app
from .models import *
from flask_login import current_user
import os

@app.route('/')
@app.route('/home')
def index():
    email = os.environ['EMAIL']

    return render_template("home.html", value=email)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/blog')
def blog():
    posts = Post.query.all()

    return render_template('blog.html', posts=posts)


@app.route('/posts/<int:id>/<string:slug>')
def individual_post(id, slug):
    user = str(current_user).strip('< >')
    post = Post.query.get_or_404(id)
    return render_template('individual_post.html', user=user, post=post)


@app.route('/contact')
def contact():
    email = 'davidarojas16@gmail.com'

    return render_template('contact.html', value=email)
