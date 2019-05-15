from mongoengine import Document, StringField


class Donor(Document):
    name = StringField()
    email = StringField()