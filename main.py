#importing required libraries
from flask import Flask, request, Response
from database.db import initialize_db
from database.models import User
from mongoengine.errors import DoesNotExist, NotUniqueError

#creating flask app object
app = Flask(__name__)

#defining URI
app.config['MONGODB_SETTINGS'] =  { 'host' : 'mongodb://localhost:27017/flask-app' }
initialize_db(app)

#creating route to print all the exsisting documents in user collection
@app.route('/list')
def print_users():
    users = User.objects().to_json()
    if len(users)>2:
        return Response(users, mimetype='application/json', status=200)
    else:
        return "No documents found"

#creating route to add new document in user collection
@app.route('/create')
def add_user():
    body = request.get_json()
    try:
        new_user = User(**body).save()
        return 'User added successfuly'
    except NotUniqueError:
        return Response('User already exist', status=400)

#creating route to update an existing document with the help of email_id
@app.route('/update/<string:email_id>', methods=['PUT'])
def update_user(email_id):
    body = request.get_json()
    try: 
    	User.objects.get(email=email_id).update(**body)
    	return 'User updated successfuly'
    except DoesNotExist:
    	return Response('User not found', status=400)

#creating route to delete an existing document by it's email_id
@app.route('/delete/<string:email_id>', methods=['DELETE'])
def delete_user(email_id):
    body = request.get_json()
    try:
        User.objects.get(email=email_id).delete()
        return 'User deleted successfuly'
    except DoesNotExist:
        return Response('User not found', status=400)


if __name__ == "__main__":
    app.run(debug=True)
