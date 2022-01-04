from flask import render_template, request
from Flask_Directory import app
from .models import *
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


@app.route('/contact')
def contact():
    email = os.environ['EMAIL']

    return render_template('contact.html', value=email)