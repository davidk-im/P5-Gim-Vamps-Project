from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

class game_move(db.Model):
    game_id = db.Column(db.Integer, primary_key=True, nullable=False)
    move = db.Column(db.Integer, nullable=False)
    usermove1 = db.Column(db.String(255), nullable=False)
    usermove2 = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=False)


class game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True, nullable=False)

def movechess(game_id, usermove1, usermove2, color):
    id = 0
    result = db.engine.execute("SELECT MAX(move) + 1 FROM game_move WHERE game_id= + " + game_id)
    for r in result:
        id = r[0]
    new_game_move = game_move(game_id=game_id, move=id, usermove1=usermove1, usermove2=usermove2, color=color)
    db.session.add(new_game_move)
    db.session.commit()
    return id

def get_next_game_id():
    id = 0
    result = db.engine.execute("SELECT MAX(game_id) + 1 FROM game")
    for r in result:
        id = r[0]
    new_game=game(game_id=id)
    db.session.add(new_game)
    new_game_move = game_move(game_id=id, move=0, usermove1="none", usermove2="none", color="none")
    db.session.add(new_game_move)
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

