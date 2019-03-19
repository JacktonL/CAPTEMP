from mongoengine import Document, StringField


class User(Document):

    name = StringField()
    email = StringField()


def createuser(name, email):

    user = User()

    user.name = name
    user.email = email

    user.save()




