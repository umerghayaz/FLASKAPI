# from datetime import datetime
#
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:umer@localhost/reciever'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# class Reciever(db.Model):
#     __tablename__ = 'reciever'
#     id = db.Column(db.Integer, primary_key = True)
#     name = db. Column(db.String(100), nullable = False)
#     message = db.Column(db.String(1000), nullable = False)
#     number = db.Column(db.Integer(), nullable = False)
#     type = db.Column(db.String(100), nullable = False)
#     last_updated = db.Column(db.DateTime, default=datetime.now())
#
#
#     def __repr__(self):
#         return "<Reciever %r>" % self.name
# if __name__ == '__main__':
#   app.run(debug=True)
def fetch():
    global data1
    data1 = 'Username'
def print_info():
    fetch()
    print(data1)
print(print_info())