from mongoengine import Document
from mongoengine.fields import BooleanField, StringField


class User(Document):
    
    fullname = StringField()
    phone_number = StringField()
    email = StringField()
    preferred_communication = StringField(choices=("SMS", "email"), default="email")
    message_sent = BooleanField(default=False)