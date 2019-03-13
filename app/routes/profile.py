from app.routes import app
from flask import render_template, session, redirect


@app.route("/profile")
def profile():

    try:
        session["displayName"]
        return render_template("profile.html")
    except KeyError:
        return redirect("/error")
