import requests
from app.routes import app
from flask import render_template, session, redirect, request, flash
from requests_oauth2.services import GoogleClient
from requests_oauth2 import OAuth2BearerToken
from .misc import usercheck, createuser, User


google_auth = GoogleClient(
    client_id=("458432068336-tocrspcbepahlmm1ovugke6hq9mqoqdf"
               ".apps.googleusercontent.com"),
    client_secret="HuUgIShcFgfT4P4YJ6IVKVKW",
    redirect_uri="http://localhost:5000/oauth2callback"
    # "http://localhost:5000/oauth2callback"
)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    if not session.get("access_token"):
        return redirect("/oauth2callback")
    with requests.Session() as s:
        s.auth = OAuth2BearerToken(session["access_token"])
        r = s.get("https://www.googleapis.com/plus/v1/people/me?access_token={}".format(session.get("access_token")))
    r.raise_for_status()
    data = r.json()
    if usercheck(data["emails"][0]['value']):
        session["displayName"] = data["displayName"]
        session["routeName"] = data["displayName"].replace(" ", "_")
        # Creates new user if display is not in a User object
        for i in User.objects():
            if i.name == data["displayName"]:
                return redirect("/")
        createuser(data["displayName"], data["emails"][0]['value'])
        return redirect("/")
    else:
        session.pop("access_token")
        flash("Must be a Oakland Tech teacher to login")
        return redirect("/error")


@app.route("/oauth2callback")
def google_oauth2callback():
    code = request.args.get("code")
    error = request.args.get("error")
    if error:
        return "error :( {!r}".format(error)
    if not code:
        return redirect(google_auth.authorize_url(
            scope=["profile", "email"],
            response_type="code",
        ))
    data = google_auth.get_token(
        code=code,
        grant_type="authorization_code",
    )
    session["access_token"] = data.get("access_token")
    return redirect("/login")


@app.route("/logout")
def logout():
    session.pop("access_token")
    session.pop("displayName")

    return redirect("/")


@app.errorhandler(404)
def page_not_found(e):
    flash("page not found")
    return render_template("error.html")
