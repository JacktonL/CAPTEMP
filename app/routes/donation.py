from app.routes import app
from flask import render_template
from .Classes import Ask, User


@app.route("/donation")
def donation():
    return render_template("donation.html", asks=list(enumerate(Ask.objects, 1)))


@app.route("/donation/<user>/<index>")
def requestpage(user, index):
    user = user.replace("_", " ")
    user = User.objects(name=user)[0]

    requests = Ask.objects(asker=user)

    request = [x for x in requests if x.index == int(index)][0]

    return render_template("requestpage.html", request=request)

