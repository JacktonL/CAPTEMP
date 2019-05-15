from app.routes.Classes import User, Donor


def displayname():
    u = [x.email for x in User.objects]
    d = [x.email for x in Donor.objects]
    return u + d
