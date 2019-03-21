from app.routes import app
from flask import render_template
from .Classes import Ask


@app.route("/donation")
def donation():
    return render_template("donation.html", asks=Ask.objects)

