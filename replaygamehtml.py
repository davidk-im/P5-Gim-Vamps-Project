from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

class game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True, nullable=False)

class replay(db.Model):
    gameID = db.Column(db.String(255), primary_key=True, nullable=False)
    usermove1 = db.Column(db.String(255), nullable=False)
    usermove2 = db.Column(db.String(255), nullable=False)
    whitemove = db.Column(db.String(255), nullable=False)
    board = db.Column(db.String(255), nullable=False)

def get_next_game_id():

    id = 0
    result = db.engine.execute("SELECT MAX(game_id) + 1 FROM game")
    for r in result:
        id = r[0]
    new_game=game(game_id=id)
    db.session.add(new_game)
    db.session.commit()
    return id


def game_create(gameID, usermove1, usermove2, whitemove, board):
    print('gameid is ' + gameID )
    new_game = gameID(gameID=gameID, usermove1=usermove1, usermove2=usermove2, whitemove=whitemove, board=board)
    db.session.add(new_game)
    db.session.commit()

def validate_replay_game(gameid):
    testid=replay.query.filter_by(gameid=gameid).first()
    if testid:
        print("game id exists")
        if testid == gameid:
            testid.is_authenticated = True
            return testid
    return None

