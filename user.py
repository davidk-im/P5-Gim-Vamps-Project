from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)



class User(db.Model):
    username = db.Column(db.String(255), primary_key=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


def user_create(username, password):
    print('User name is ' + username + ' and password is ' + password)

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
