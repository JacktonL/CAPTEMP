from app.routes import app
from flask import render_template, session, redirect, request, flash
from .Forms import Request
from .Classes import Ask, User
from .misc import displayname, indexer


@app.route("/profile", methods=["GET", "POST"])
def profile():
    user = 0
    try:
        if session["displayName"] in displayname():
            user = User.objects(name=session["displayName"])[0]
    except KeyError:
        return redirect("/error")

    form = Request(request.form)
    if request.method == 'POST' and form.validate():
            newask = Ask()
            newask.asker = user
            newask.item_name = form.item_name.data
            newask.description = form.description.data
            user.reload()
            user.update(asks=user.asks+1)
            newask.index = user.asks + 1
            newask.save()

    return render_template("profile.html", form=form, asks=enumerate(Ask.objects(asker=user), 1))


@app.route("/delete/<index>")
def delete(index):
    try:
        index = int(index)

    except ValueError:
        flash("Unknown Index")
        return render_template("error.html")

    user = User.objects(name=session["displayName"])[0]
    asks = Ask.objects(asker=user)

    for i in asks:
        if index == i.index:
            i.delete()
            indexer(user)
            if len(asks) == 1:
                user.update(asks=0)
            else:
                user.update(asks=len(asks)-1)
            return redirect("/profile")


@app.route("/user/<user>")
def profilepage(user):
    user = user.replace("_", " ")
    user = User.objects(name=user)[0]
    asks = Ask.objects(asker=user)

    return render_template("userpage.html", user=user, asks=enumerate(asks, 1))
