from flask import render_template, request
from Flask_Directory import app


# ADMIN login page and authentication
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('my_signup.html')