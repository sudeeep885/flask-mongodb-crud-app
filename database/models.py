from .db import db

# creating user collection
class User(db.Document): #inheriting from Document class

    email = db.EmailField(unique=True)
    name = db.StringField(required=True)
    company_name = db.StringField(required=True)
    mobile_no = db.IntField(required=True)

    meta = {
        "indexes" : ["email"]  # adding email as an index
    }