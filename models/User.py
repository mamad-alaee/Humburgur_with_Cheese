from mongoengine import Document , StringField,ReferenceField
from models.Role import Role

class User(Document):
    full_name = StringField(required=True)
    password = StringField(required=True)
    email = StringField(required=True)
    role = ReferenceField(Role)