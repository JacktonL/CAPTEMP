import os
from flask import Flask
from mongoengine import connect

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or os.urandom(20)


from .routes import *
