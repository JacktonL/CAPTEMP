from app.routes import app
from flask import render_template
from .Classes import Ask


@app.route("/donation")
def donation():
    return render_template("donation.html", asks=list(enumerate(Ask.objects, 1)))


@app.route("/request/<request>")
def requestpage(request):

    return render_template("requestpage.html", request=request)

