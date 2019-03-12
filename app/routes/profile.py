from app.routes import app
from flask import render_template, session


@app.route("/profile")
def profile():

    if session["displayName"]:
        return render_template("profile.html")
    else:
        return "Login"
