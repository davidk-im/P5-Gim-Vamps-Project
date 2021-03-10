from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

class game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True, nullable=False)

class game_move(db.Model):
    game_move_id = db.Column(db.Integer, primary_key=True, nullable=False)
    game_id = db.Column(db.Integer, nullable=False)
    move = db.Column(db.Integer, nullable=False)
    usermove1 = db.Column(db.String(255), nullable=False)
    usermove2 = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=False)

def save_game_move(game_id, move, usermove1, usermove2, color):
    id = game_id * 1000 + move
    new_game_move=game_move(game_move_id=id, game_id=game_id, move=move, usermove1=usermove1, usermove2=usermove2, color=color)
    db.session.add(new_game_move)
    db.session.commit()


#def delete_move(usermove1, usermove2):


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

def get_game_replay(game_id):
    results=game_move.query.filter_by(game_id=game_id).order_by(game_move.move)
    return results


