from flask_mongoengine import MongoEngine #importting mongoengine

db = MongoEngine() #creating mongoengine object

# function to initialize mongoengine object with flask app object
def initialize_db(app):
    db.init_app(app)