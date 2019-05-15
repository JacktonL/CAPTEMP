from app.routes.Classes import Donor


def donorcreate(name, email):

    donor = Donor()

    donor.name = name
    donor.email = email

    donor.save()
