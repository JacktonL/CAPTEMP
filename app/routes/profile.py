from app.routes import app
from flask import render_template, session, redirect, request
from .Forms import Request
from .Classes import Ask, User


@app.route("/profile", methods=["GET", "POST"])
def profile():

    try:
        session["displayName"]
    except KeyError:
        return redirect("/error")

    form = Request(request.form)
    if request.method == 'POST' and form.validate():
        for i in User.objects:
            if i.name == session["displayName"]:
                newask = Ask()
                newask.asker = i
                newask.item_name = form.item_name.data
                newask.description = form.description.data
                newask.save()

    return render_template("profile.html", form=form)

