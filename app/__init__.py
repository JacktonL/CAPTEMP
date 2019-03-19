import os
from flask import Flask
from mongoengine import connect

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or os.urandom(20)
connect('otdonations', host="mongodb://admin:1admin@ds012889.mlab.com:12889/otdonations")


from .routes import *
