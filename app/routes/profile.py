from app.routes import app
from flask import render_template, session, redirect, request
from .Forms import Request
from .Classes import Ask, User
from .misc import displayname


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

