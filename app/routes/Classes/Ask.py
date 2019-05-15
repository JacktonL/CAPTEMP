from mongoengine import Document, StringField, ReferenceField, IntField, BooleanField
from .User import User
from .Donor import Donor


class Ask(Document):

    asker = ReferenceField(User)
    item_name = StringField()
    description = StringField()
    index = IntField()
    complete = BooleanField()
    donor = ReferenceField(Donor)
