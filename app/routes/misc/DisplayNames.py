from app.routes.Classes import User


def displayname():
    return [x.name for x in User.objects]
