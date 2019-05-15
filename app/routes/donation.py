from app.routes import app
from flask import render_template, redirect
from .Classes import Ask, User, Donor


@app.route("/donation")
def donation():
    return render_template("donation.html", asks=list(enumerate(Ask.objects(complete=False), 1)))


@app.route("/donation/<user>/<index>")
def requestpage(user, index):
    user = user.replace("_", " ")
    user = User.objects(name=user)[0]

    requests = Ask.objects(asker=user)

    request = [x for x in requests if x.index == int(index)][0]

    return render_template("requestpage.html", request=request)


@app.route("/donate/<user>/<index>/<donor>")
def donate(user, index, donor):
    donor = donor.replace("_", " ")
    user = user.replace("_", " ")
    index = int(index)

    donor = Donor.objects(name=donor)[0]
    user = User.objects(name=user)[0]
    ask = Ask.objects(asker=user)
    ask = [i for i in ask if i.index == index][0]
    ask.reload()
    ask.update(donor=donor, complete=True)

    return redirect("/donation/{}/{}".format(user.name.replace(" ", "_"), index))

