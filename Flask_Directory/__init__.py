from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_ckeditor import CKEditor, CKEditorField
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ['SECRET_KEY']

# Connecting PostgreSQL using SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URI']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Bootstrap(app)
ckeditor = CKEditor(app)

# Configuring login manager to allow admin login for blog posting
from .models import User

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


from Flask_Directory import routes, auth
