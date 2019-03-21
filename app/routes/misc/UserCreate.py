from app.routes.Classes import User


def createuser(name, email):

    user = User()

    user.name = name
    user.email = email

    user.save()




