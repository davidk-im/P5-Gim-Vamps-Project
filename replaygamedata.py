from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)



class Replay(db.Model):
    gameID = db.Column(db.String(255), primary_key=True, nullable=False)
    movenumber = db.Column(db.String(255), nullable=False)
    blackmove = db.Column(db.String(255), nullable=False)
    whitemove = db.Column(db.String(255), nullable=False)

def game_create(gameID, movenumber, colormove, move):
    print('Game ID: ' + gameID )

    new_game = gameID(gameID=gameID, movenumber=movenumber, blackmove=blackmove, whitemove=whitemove)
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
