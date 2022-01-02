from flask import Flask
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ['SECRET_KEY']

from Flask_Directory import routes, auth
