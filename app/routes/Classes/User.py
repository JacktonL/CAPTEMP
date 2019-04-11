from mongoengine import Document, StringField, IntField


class User(Document):

    name = StringField()
    email = StringField()
    asks = IntField(default=0)
