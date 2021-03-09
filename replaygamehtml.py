from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)



class replay(db.Model):
    gameID = db.Column(db.String(255), primary_key=True, nullable=False)
    usermove1 = db.Column(db.String(255), nullable=False)
    usermove2 = db.Column(db.String(255), nullable=False)
    whitemove = db.Column(db.String(255), nullable=False)
    board = db.Column(db.String(255), nullable=False)



def game_create(gameID, usermove1, usermove2, whitemove, board):
    print('gameid is ' + gameID )
    new_game = gameID(gameID=gameID, usermove1=usermove1, usermove2=usermove2, whitemove=whitemove, board=board)
    db.session.add(new_game)
    db.session.commit()

def validate_replay_game(gameid):
    testid=replay.query.filter_by(gameid=gameid).first()
    if testid:
        print("test id exists")
        if testid == gameid:
            testid.is_authenticated = True
            return testid
    return None

