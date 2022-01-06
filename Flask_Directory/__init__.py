from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = '7Hsjd93p9dlo-39asdmOSD9sd-P39GMipgsjwi52'

# Connecting PostgreSQL using SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://ftjxavnyyhxsxi:34175001066c4680f3234f47210575ccedcd44e9f342e598' \
                                        '8c13f5a256fb9deb@ec2-44-198-211-34.compute-1.amazonaws.com:5432/d4ap67kh802935'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Configuring login manager to allow admin login for blog posting
from .models import User

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


from Flask_Directory import routes, auth
