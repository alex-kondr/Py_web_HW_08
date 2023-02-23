from mongoengine import Document
from mongoengine.fields import BooleanField, StringField


class User(Document):
    fullname = StringField()
    phone_number = StringField()
    email = StringField()
    message_sent = BooleanField(default=False)