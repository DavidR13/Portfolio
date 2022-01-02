from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "7Hsjd93p9dlo-39asdmOSD9sd-P39GMipgsjwi52"

from Flask_Directory import routes, auth
