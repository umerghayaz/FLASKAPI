# This is a sample Python script.
# app.py
# from flask import Flask, render_template, request, redirect, url_for, flash
# import psycopg2  # pip install psycopg2
# import psycopg2.extras
# # from flask.ext.sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.secret_key = "cairocoders-ednalan"
#
# DB_HOST = "localhost"
# DB_NAME = "demodb"
# DB_USER = "postgres"
# DB_PASS = "umer"
#
# conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
#
#
# @app.route('/')
# def Index():
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     s = "SELECT * FROM students"
#     cur.execute(s)  # Execute the SQL
#     list_users = cur.fetchall()
#     return render_template('index.html', list_users=list_users)
#
#
# @app.route('/add_student', methods=['POST'])
# def add_student():
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     if request.method == 'POST':
#         fname = request.form['fname']
#         lname = request.form['lname']
#         email = request.form['email']
#         cur.execute("INSERT INTO students (fname, lname, email) VALUES (%s,%s,%s)", (fname, lname, email))
#         conn.commit()
#         flash('Student Added successfully')
#         return redirect(url_for('Index'))
#
#
# @app.route('/edit/<id>', methods=['POST', 'GET'])
# def get_employee(id):
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#
#     cur.execute('SELECT * FROM students WHERE id = %s', (id))
#     data = cur.fetchall()
#     cur.close()
#     print(data[0])
#     return render_template('edit.html', student=data[0])
#
#
# @app.route('/update/<id>', methods=['POST'])
# def update_student(id):
#     if request.method == 'POST':
#         fname = request.form['fname']
#         lname = request.form['lname']
#         email = request.form['email']
#
#         cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         cur.execute("""
#             UPDATE students
#             SET fname = %s,
#                 lname = %s,
#                 email = %s
#             WHERE id = %s
#         """, (fname, lname, email, id))
#         flash('Student Updated Successfully')
#         conn.commit()
#         return redirect(url_for('Index'))
#
#
# @app.route('/delete/<string:id>', methods=['POST', 'GET'])
# def delete_student(id):
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#
#     cur.execute('DELETE FROM students WHERE id = {0}'.format(id))
#     conn.commit()
#     flash('Student Removed Successfully')
#     return redirect(url_for('Index'))
#
#
# if __name__ == "__main__":
#     app.run(debug=True,port=8000)
# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://wslnapfcxanodr:a7264b32be99407001919e87affb1e06e86a4f8a844daa4eb722678aed8d4cfe@ec2-54-163-34-107.compute-1.amazonaws.com:5432/dfb4pqic2dqauj'
#
# db=SQLAlchemy(app)
#
# # Create our database model
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, email):
#         self.email = email
#
#     def __repr__(self):
#         return '<E-mail %r>' % self.email
#
# # Set "homepage" to index.html
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # Save e-mail to database and send to success page
# @app.route('/prereg', methods=['POST'])
# def prereg():
#     email = None
#     if request.method == 'POST':
#         email = request.form['email']
#         # Check that email does not already exist (not a great query, but works)
#         if not db.session.query(User).filter(User.email == email).count():
#             reg = User(email)
#             db.session.add(reg)
#             db.session.commit()
#             print('hello')
#             return render_template('success.html')
#     return render_template('index.html')
#
# if __name__ == '__main__':
#     app.debug = True
#     app.run()
# reources
# https://github.com/kanuarj/flaskMongo/blob/master/app.py
# https://webninjadeveloper.com/python/build-a-python-crud-rest-api-in-flask-and-mongodb-using-flask-pymongo-library-in-browser/
import json
import os
from datetime import datetime

from Scripts.bottle import redirect
from bson import ObjectId
from flask import Flask, request, jsonify, abort, url_for, flash
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import mongoengine
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask import jsonify,request

# import cors as cors
from flask_cors import CORS
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://wslnapfcxanodr:a7264b32be99407001919e87affb1e06e86a4f8a844daa4eb722678aed8d4cfe@ec2-54-163-34-107.compute-1.amazonaws.com:5432/dfb4pqic2dqauj'
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'crud',
#     'host': 'localhost',
#     'port': 27017
# }
app.config['MONGO_URI'] = "mongodb://localhost:27017/User"
# app.config['MONGO_DBNAME'] = 'user'
app.secret_key = "umer"
mongo = PyMongo(app)
customer_collection = mongo.db.user

db = MongoEngine()
db.init_app(app)

# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)
#
# CORS(app)
# # class Recipe(db.Model):
# #     __tablename__ = "recipe"
# #     id = db.Column(db.Integer, primary_key=True)
# #     recipe = db.Column(db.JSON)
# class Reciever(db.Document):
#
#     name = db.StringField()
#     message = db.StringField()
#     number = db.StringField()
#     type = db.StringField()
# #     latitude = db.Column(db.Float,index=False,unique=False)
# #     date = db.Column(db.DateTime, default=datetime.now())
# # class Image(db.Model):
# #     __tablename__ = "image"
# #     id = db.Column(db.Integer, primary_key=True)
# #     profile_pic = db.Column(db.String(100))
#
#     #     return redirect(request.url)
# # class Sender(db.Model):
# #     __tablename__ = 'sender'
# #     id = db.Column(db.Integer, primary_key = True)
# #     name = db. Column(db.String(100), nullable = False)
# #     message = db.Column(db.String(1000), nullable = False)
# #     number = db.Column(db.Integer(), nullable = False)
# #     type = db.Column(db.String(100), nullable = False)
# @cross_origin()
@app.route('/pets', methods=['POST'])
@cross_origin()
# for inserting data
def create_pet():
    pet_data = request.get_json()
    name = pet_data['name']
    message = pet_data['message']
    number = pet_data['number']
    type = pet_data['type']
    customer_collection.insert_one({'name' : name, 'message' : message, 'number' : number,'type':type})
    return jsonify({"success": True, "response": "Pet added"})
    # pet.save()
    # db.session.add(pet)
    # db.session.commit()
    # print(name)
    # response = messenger.send_message(message, type)
    # response = messenger.send_audio(
    #     message,
    #     recipient_id=type,
    # )
    # date = pet_data['date']



#     def __repr__(self):
#         return "<Reciever %r>" % self.name
#
from flask import jsonify,request
from bson.json_util import dumps
# for viewing data
@cross_origin()

@app.route('/getdata', methods = ['GET'])
def retrieveAll():
    # users = mongo.db.user.find()
    #
    # resp = dumps(users)
    # return resp
    holder = list()
    # # currentCollection = mongo.db.user
    for i in customer_collection.find():
        print(i)
        holder.append({'name':i['name'], 'message' : i['message'], 'number' : i['number'],'type' : i['type']})
    return jsonify(holder)
@app.route('/getdata', methods = ['GET'])
# def retrieveAll():
#     # users = mongo.db.user.find()
#     #
#     # resp = dumps(users)
#     # return resp
#     holder = list()
#     # # currentCollection = mongo.db.user
#     for i in customer_collection.find():
#         print(i)
#         holder.append({'name':i['name'], 'message' : i['message'], 'number' : i['number'],'type' : i['type']})
#     return jsonify(holder)
# for viewing data
@app.route('/getpets/<name>', methods = ['GET'])
@cross_origin()
def retrieveFromName(name):
    # currentCollection = mongo.db.favInfo
    data = customer_collection.find_one_or_404({"name":name})
    return jsonify({'name': data['name'],'id':data['id'] ,'message': data['message'], 'number': data['number'],'type': data['type']})
    # resp = dumps(data)
    # return resp
    # holder = list()
    # # for i in customer_collection.find_one({"name" : name}):
    # #     # return jsonify(i)
    # #     holder.append({'name':i['name'], 'message' : i['message'], 'number' : i['number'],'type' : i['type']})
    # return jsonify(data)
# from bson.objectid import ObjectId
@cross_origin()
@app.route('/update/<name>', methods = ['PUT'])
def updateData(name):

    updatedName = request.json['name']
    customer_collection.update_one({'name':name}, {"$set" : {'name' : updatedName}})
    return jsonify({"success": True, "response": "Pet added"})
# for updating data
@cross_origin()
@app.route('/updateDatamany/<id>', methods=['PUT'])
def updateDatamany(id):
    _id = id
    pet_data = request.get_json()
    name = pet_data['name']
    message = pet_data['message']
    number = pet_data['number']
    type = pet_data['type']
    customer_collection.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
                             {'$set': {'name': name, 'message': message, 'number:': number,'type':type}})

    return jsonify({"success": True, "response": "updated successfully"})
# for viewing data
@cross_origin()
@app.route('/users/<id>')
def user(id):
    user = customer_collection.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp
@cross_origin()
@app.route('/users')
def users():
    user = customer_collection.find_one()
    resp = dumps(user)
    return resp
# for deleting data
# @cross_origin()
@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    customer_collection.delete_one({'_id': ObjectId(id)})
    resp = jsonify("User deleted successfully")
    resp.status_code = 200
    return resp
    # message = request.json['message']
    # number = request.json['number']
    # type = request.json['type']
    # customer_collection.update_one(
    #     {'name':name},
    #     {
    #         "$set": {
    #             "type": type,
    #             "message": message,
    #             "number": number
    #         }
    #     }
    # )
    # for i in customer_collection.find():
        # customer_collection.update_many({'number':i['number'], 'message' : i['message']}, {"$set" : {'number' : updatednumber,'message':updatedmessage}})
@cross_origin()
@app.route('/getpets/<name>', methods = ['GET'])
def get_one_movie(name: str):
    movie = Reciever.objects(name=name).first()
    return jsonify(movie), 200
@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    movie = Reciever.objects.get_or_404(id=id)
    movie.delete()
    return jsonify(str(movie.id)), 200
@app.route('/movies11/<id>', methods=['POST'])
def update_movie(id):

    movie = Reciever.objects(id=id).first()
    if not movie:
        return jsonify({'error': 'data not found'})
    else:
        body = request.get_json()
        movie.update(name=body['name'],number=body['number'],type=body['type'])
    return jsonify(movie), 200
    # if movie:
    #     body = request.get_json()
    #     director = Reciever()
    #     director.name = body.get("name")
    #     director.number = body.get("number")
    #     director.type = body.get("type")
    #     director.save()
    #     movie.save()
    # movie.update(**body)
# @app.route('/getpets', methods = ['GET'])
# def getpets():
#      all_pets = []
#      pets = Reciever.objects(_id=Reciever.id).first()
#      return jsonify(pets), 200
     # for pet in pets:
     #      results = {"id":pet.id,
     #                "name":pet.name,
     #                "message":pet.message,
     #                "number":pet.number,
     #                "type":pet.type,
     #                 }
     #      all_pets.append(results)
     #
     # return jsonify(
     #        {
     #            "success": True,
     #            "pets": all_pets,
     #            "total_pets": len(pets),
     #        }
     #    )
# @cross_origin()
# @app.route("/pets/<int:pet_id>", methods = ["PATCH"])
# def update_pet(pet_id):
#     pet = Reciever.query.get(pet_id)
#     pet.save()
#     # db.session.delete(pet)
#     # db.session.commit()
#     return jsonify({"success": True, "response": "delete"})
# # @cross_origin()
# # @app.route('/js', methods=['POST'])
# # def create_js():
# #     per_1 = Recipe(recipe={'object': 'whatsapp_business_account', 'entry': [{'id': '110664218507574', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '15550813755', 'phone_number_id': '110829038490956'}, 'contacts': [{'profile': {'name': 'umer'}, 'wa_id': '923462901820'}], 'messages': [{'from': '923462901820', 'id': 'wamid.HBgMOTIzNDYyOTAxODIwFQIAEhgUM0VCMEM4RkFFQzQxN0FFRjQ4RjIA', 'timestamp': '1668859762', 'text': {'body': 'hello'}, 'type': 'text'}]}, 'field': 'messages'}]}]})
# #     db.session.add(per_1)
# #     db.session.commit()
# #     return jsonify({"success": True, "response": "Pet added"})
# #     def __repr__(self):
# #         return "<Reciever %r>" % self.name
# # per_1 = Recipe(recipe={'object': 'whatsapp_business_account', 'entry': [{'id': '110664218507574', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '15550813755', 'phone_number_id': '110829038490956'}, 'contacts': [{'profile': {'name': 'umer'}, 'wa_id': '923462901820'}], 'messages': [{'from': '923462901820', 'id': 'wamid.HBgMOTIzNDYyOTAxODIwFQIAEhgUM0VCMEM4RkFFQzQxN0FFRjQ4RjIA', 'timestamp': '1668859762', 'text': {'body': 'hello'}, 'type': 'text'}]}, 'field': 'messages'}]}]})
# # db.session.add(per_1)
# # db.session.commit()
# if __name__ == '__main__':
#   app.run(debug=True)
# import json
# from flask import Flask, request, jsonify
# from flask_mongoengine import MongoEngine
#
# app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'crud',
#     'host': 'localhost',
#     'port': 27017
# }
# db = MongoEngine()
# db.init_app(app)
#
# class User(db.Document):
#     name = db.StringField()
#     email = db.StringField()
#     def to_json(self):
#         return {"name": self.name,
#                 "email": self.email}
#
# @app.route('/get', methods=['GET'])
# def query_records():
#     name = request.args.get('name')
#     user = User.objects(name=name).first()
#     if not user:
#         return jsonify({'error': 'data not found'})
#     else:
#         return jsonify(user.to_json())
#
# @app.route('/add', methods=['POST'])
# def create_record():
#     record = json.loads(request.data)
#     user = User(name=record['name'],
#                 email=record['email'])
#     user.save()
#     return jsonify(user.to_json())
#
# @app.route('/', methods=['POST'])
# def update_record():
#     record = json.loads(request.data)
#     user = User.objects(name=record['name']).first()
#     if not user:
#         return jsonify({'error': 'data not found'})
#     else:
#         user.update(email=record['email'])
#     return jsonify(user.to_json())
#
# @app.route('/', methods=['DELETE'])
# def delete_record():
#     record = json.loads(request.data)
#     user = User.objects(name=record['name']).first()
#     if not user:
#         return jsonify({'error': 'data not found'})
#     else:
#         user.delete()
#     return jsonify(user.to_json())
#
if __name__ == "__main__":
    app.run(debug=True)