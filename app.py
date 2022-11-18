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
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:umer@localhost/pre-registration'

db=SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()