from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
#from models import login_manager

app = Flask(__name__)
db = SQLAlchemy(app)



class User(db.Model):
    username = db.Column(db.String(255), primary_key=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    tactics_elo = db.Column(db.Integer, nullable=False)
    tactics_streak = db.Column(db.Integer, nullable=False)
    multiplayer_elo = db.Column(db.Integer, nullable=False)

TACTICS_ELO_DEFAULT = 1500
TACTICS_STREAK_DEFAULT = 0
MULTIPLAYER_ELO_DEFAULT = 1500
def user_create(username, password):
    print('User name is ' + username + ' and password is ' + password)

    new_user = User(username=username, password=password, tactics_elo=TACTICS_ELO_DEFAULT, tactics_streak=TACTICS_STREAK_DEFAULT, multiplayer_elo=MULTIPLAYER_ELO_DEFAULT)
    db.session.add(new_user)
    db.session.commit()

def user_update_stats(username, tactics_elo, tactics_streak, multiplayer_elo):
    user = User.query.filter_by(username=username).first()
    user.tactics_elo=tactics_elo
    user.tactics_streak=tactics_streak
    user.multiplayer_elo=multiplayer_elo
    db.session.commit()