from app.routes import app
from flask import render_template


@app.route("/donation")
def donation():
    return render_template("donation.html")

