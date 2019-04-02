from mongoengine import Document, StringField, ReferenceField
from .User import User


class Ask(Document):

    asker = ReferenceField(User)
    item_name = StringField()
    description = StringField()

