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
import os
from datetime import datetime

from Scripts.bottle import redirect
from flask import Flask, request, jsonify, abort, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'

# import cors as cors
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://wslnapfcxanodr:a7264b32be99407001919e87affb1e06e86a4f8a844daa4eb722678aed8d4cfe@ec2-54-163-34-107.compute-1.amazonaws.com:5432/dfb4pqic2dqauj'
# from heyoo import WhatsApp
# whatsapp = WhatsApp('EAAJVc3j40G8BABLa7dKqetvZC3lKyCKYnSI1gIaqUKLv6ZAZBkVHN3qv4rZCmkT4DZBhZCcEYZAfOpeLLLu2D2XUtWtg3js7HHFZCZB3DATSQycjtnt7n9c7YzTyea5BMcdEINDZCBo3nBQL95q639jjCeLHtlABeihzMzPEOkgSInNmnx9D9MefmkodOQwieFbXIPIVjsSmVFYAZDZD', '110829038490956')
# l=whatsapp.query_media_url('844082013517554')
# mime_type='application/pdf'
# l=whatsapp.download_media(l ,mime_type)
# l
from heyoo import WhatsApp
# messenger = WhatsApp('EAAJVc3j40G8BADf4NEUa4wRxZCnZBbFDZCgx05b4rC90uJTRBfOzWiQZBha4USjh2M8fVDZA8HKQLYkZBLzxZCF8yZBZAVANpYIdqJyUupAFwaSY3fHtl3WebpnIO9dT9swq6507YsUyC8fyAP7mBeqnZCbBsAaNn6FLLTllksejCNHfMZAeZB1khrGFGfbiGgfZCMSLoYPv4q4ZALkwZDZD',phone_number_id='110829038490956')
# For sending a Text messages
# response =messenger.send_message('https://a0b5-116-0-56-98.in.ngrok.io/static/uploads/59ecf216-1fcf-4223-ae17-09595cf23fc9.jpeg', '923462901820')
# For sending an Image
# messenger.send_image(
#         image="https://i.imgur.com/YSJayCb.jpeg",
#         recipient_id="91989155xxxx",
#     )
# print(response)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from flask_cors import CORS, cross_origin

CORS(app)
# class Recipe(db.Model):
#     __tablename__ = "recipe"
#     id = db.Column(db.Integer, primary_key=True)
#     recipe = db.Column(db.JSON)
# class Reciever(db.Model):
#     __tablename__ = 'reciever122'
#     id = db.Column(db.Integer, primary_key = True)
#     name = db. Column(db.String(100), nullable = False)
#     message = db.Column(db.String(1000), nullable = False)
#     number = db.Column(db.Integer(), nullable = False)
#     type = db.Column(db.String(100), nullable = False)
#     latitude = db.Column(db.Float,index=False,unique=False)
#     date = db.Column(db.DateTime, default=datetime.now())
# class Image(db.Model):
#     __tablename__ = "image"
#     id = db.Column(db.Integer, primary_key=True)
#     profile_pic = db.Column(db.String(100))


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','wav'])
# db = MongoEngine()
# db.init_app(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     # l = whatsapp.query_media_url('844082013517554')
#     # mime_type = 'application/pdf'
#     # l = whatsapp.download_media(l, mime_type)
#     # l
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)
#     file = request.files['file']
#
#     # file = l
#     print(file)
#     if file.filename == '':
#         flash('No image selected for uploading')
#         return redirect(request.url)
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         # file.save(secure_filename(file.filename))
#         usersave = Image( profile_pic=file.filename)
#         db.session.add(usersave)
#         db.session.commit()
#         print('upload_image filename: ' + filename)
#         flash('Image successfully uploaded and displayed below')
#         o=url_for('static', filename='uploads/' + filename)
        # l = 'https://myupla.herokuapp.com/'+url_for('static', filename='uploads/' + filename)
        # print('url is',l)

    #     return redirect(url_for('static', filename='uploads/' + filename), code=301)
    # else:
    #     flash('Allowed image types are -> png, jpg, jpeg, gif')
    #     return redirect(request.url)
class Sender(db.Model):
    __tablename__ = 'sender'
    id = db.Column(db.Integer, primary_key = True)
    name = db. Column(db.String(100), nullable = False)
    message = db.Column(db.String(1000), nullable = False)
    number = db.Column(db.Integer(), nullable = False)
    type = db.Column(db.String(100), nullable = False)
@cross_origin()
@app.route('/pets', methods=['POST'])
def create_pet():
    pet_data = request.get_json()

    name = pet_data['name']
    message = pet_data['message']
    number = pet_data['number']
    type = pet_data['type']
    # response = messenger.send_message(message, type)
    # response = messenger.send_audio(
    #     message,
    #     recipient_id=type,
    # )
    # date = pet_data['date']
    pet = Sender(name=name, message=message, number=number, type=type)
    db.session.add(pet)
    db.session.commit()

    return jsonify({"success": True, "response": "Pet added"})
    def __repr__(self):
        return "<Reciever %r>" % self.name

# @cross_origin()
# @app.route('/getpets', methods = ['GET'])
# def getpets():
#      all_pets = []
#      pets = Reciever.query.all()
#      for pet in pets:
#           results = {
#                     "name":pet.name,
#                     "message":pet.message,
#                     "number":pet.number,
#                     "type":pet.type,
#                      }
#           all_pets.append(results)
#
#      return jsonify(
#             {
#                 "success": True,
#                 "pets": all_pets,
#                 "total_pets": len(pets),
#             }
#         )
# @cross_origin()
# @app.route("/pets/<int:pet_id>", methods = ["PATCH"])
# def update_pet(pet_id):
#     pet = Reciever.query.get(pet_id)
#     db.session.delete(pet)
#     db.session.commit()
#     return jsonify({"success": True, "response": "delete"})
# @cross_origin()
# @app.route('/js', methods=['POST'])
# def create_js():
#     per_1 = Recipe(recipe={'object': 'whatsapp_business_account', 'entry': [{'id': '110664218507574', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '15550813755', 'phone_number_id': '110829038490956'}, 'contacts': [{'profile': {'name': 'umer'}, 'wa_id': '923462901820'}], 'messages': [{'from': '923462901820', 'id': 'wamid.HBgMOTIzNDYyOTAxODIwFQIAEhgUM0VCMEM4RkFFQzQxN0FFRjQ4RjIA', 'timestamp': '1668859762', 'text': {'body': 'hello'}, 'type': 'text'}]}, 'field': 'messages'}]}]})
#     db.session.add(per_1)
#     db.session.commit()
#     return jsonify({"success": True, "response": "Pet added"})
#     def __repr__(self):
#         return "<Reciever %r>" % self.name
# per_1 = Recipe(recipe={'object': 'whatsapp_business_account', 'entry': [{'id': '110664218507574', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '15550813755', 'phone_number_id': '110829038490956'}, 'contacts': [{'profile': {'name': 'umer'}, 'wa_id': '923462901820'}], 'messages': [{'from': '923462901820', 'id': 'wamid.HBgMOTIzNDYyOTAxODIwFQIAEhgUM0VCMEM4RkFFQzQxN0FFRjQ4RjIA', 'timestamp': '1668859762', 'text': {'body': 'hello'}, 'type': 'text'}]}, 'field': 'messages'}]}]})
# db.session.add(per_1)
# db.session.commit()
if __name__ == '__main__':
  app.run(debug=True)