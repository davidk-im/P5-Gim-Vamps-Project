#imports
from flask import (Flask, g, redirect, render_template, request, session, url_for)
from user import user_create
from flask_sqlalchemy import SQLAlchemy
import requests
import chessdata
from chessdata import board, movelist, og_board, ogstoreboard, movesdata, actualMove, previousMove, getMove, didMove, getUserMove2, getUserMove1, getColor
from markupsafe import escape
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from user import validate_user, User, user_create, user_update_stats
from htmlToPythonAdditions import HTPlen5
import getpass
import mysql.connector
import webbrowser
import random
import time
from replaygamehtml import get_next_game_id, save_game_move, get_game_replay
from htmlToPython import htmlToPython



app = Flask(__name__)


# database setup
dbURI = 'sqlite:///chess.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)
db.init_app(app)

#conn = mysql.connector.connect(user='root', password='',
                               #host='localhost',database='company')

#if conn:
    #print ("Connected Successfully")
#else:
    #print ("Connection Not Established")

#login setup
app.config['SECRET_KEY'] = '1234'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#using login_manager.user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()


#route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        #username and password variables from form
        username = request.form['Username']
        password = request.form['password']
        #just to check if username and password was collected
        print(username +" " + password)
        #calls validate_user function from user.py
        user = validate_user(username, password)

        if user:
            #if validate_user = true, log user in and return profile.html template
            login_user(user)
            db.session.commit()
            #variables that are called in profile.html
            session['user_name'] = user.username
            session['tactics_elo'] = user.tactics_elo
            session['tactics_streak'] = user.tactics_streak
            session['multiplayer_elo'] = user.multiplayer_elo
            return render_template("profile.html")
    else:
        print('Bar')
        #if validate_user = false, return login page
    return render_template("login.html")


#route for profile page
#@login_required tag used to ensure that user cannot access profile if not signed in
@app.route('/profile')
@login_required
def profile():
        return render_template('profile.html', name=current_user.username)

#route for logging out
#@login_required tag used to ensure that user must be logged in to log out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.html'))


#sign up page route
@app.route('/signup' ,methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        #get username and password from form
        username = request.form['Username']
        password = request.form['password']
        #calls user_create function from user.py
        user_create(username, password)
        #returns signconfirm.html(signup confirmation page)
        return render_template("signconfirm.html")
        db.session.commit()

    else:
        print('Bar')
        #if for some reason form doesn't go through for some reason, returns signup page again
    return render_template("signup.html")

#sign up success page returned after post process above
@app.route('/signupsuccess')
def signconfirm():
    return render_template("signconfirm.html")


#route to replay a chess game
@app.route('/replaygame' , methods= ['POST', 'GET'])
def replaygame():
    if request.method=='POST':
        game_id = request.form['game_id']
        print(game_id)
        replay=get_game_replay(game_id)
        if replay.count() >0:
            return render_template("replaygamedata.html", replay=replay, game_id=game_id)
    #else:
        #print('Bar')
    return render_template("replaygame.html")

#route to join a chess game
@app.route('/joingame')
def joingame():
    return render_template("joingame.html")

#chess offline website leaderboards
@app.route('/leaderboards')
def leaderboards():
    users = User.query.order_by(User.tactics_elo.desc()).all()
    ranks = dict()
    rank = 1
    for u in users:
        print(u)
        ranks[u.username] = rank
        rank += 1
    return render_template("leaderboards.html",rows=users,ranks=ranks)



#web api route where data is grabbed from different types of chess
@app.route('/lichesslb/<type>/', methods=['GET', 'POST'])
def lichesslb(type):
    print(type)
    url = "https://lichess.org/player/top/100/" + type + "/"
    headers = {
        'Accept': 'application/vnd.lichess.v3+json'
    }
    response = requests.get(url, headers=headers)
    data = response.json().get('users')
    type = type.capitalize()
    return render_template("webapi2.html", data=data, type=type)



#Chess code
@app.route("/createBoardTable", methods=['GET','POST']) #this is is where the website directs to when clicking the submit button
def createBoardTable():
    if request.method == 'POST': #if the meathod is post
        form = request.form
        movelist.clear()#resets the stored moves when create board is selected
        board = og_board #resets the board
        storeboard = dict(ogstoreboard) #resets the storboard
        return render_template("chessDicTtableMulti.html", displayClicked="  ", allBoard=chessdata.split_board(board))


@app.route("/board/<space>", methods=['GET','POST'])
def boardprint(space):
    if request.method == 'POST':
        #moves piece
        sets = chessdata.movesdata(space)
        game_id=session['game_id']
        if chessdata.didMove():
            um1=chessdata.getUserMove1()
            um2=chessdata.getUserMove2()
            wm=chessdata.getColor()
            if htmlToPython(um1, um2, wm, board) != "invalid":

                game_id = session['game_id']
            save_game_move(game_id, chessdata.getMove(), um1, um2, wm)
        return render_template("chessDicTtableMulti.html", displayClicked=space, movelist=sets,  message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))

@app.route('/chessDicTtableMulti')
def chessDicTtableMulti():
    return render_template("chessDicTtableMulti.html")


@app.route('/multiplayermain')
def multiplayermain():
    return render_template("multiplayermain.html")


#multiplayer chess game route
@app.route('/MultiplayerMenu' , methods=['GET' , 'POST'])
def MultiplayerMenu():
    if request.method == 'POST':
        session['game_id'] = get_next_game_id()
        return render_template("multiplayermain.html")

    return render_template("MultiplayerMenu.html")

@app.route('/ai')
def ai():
    #htmltopythonai
    #set variables: aicolor = B/W
    return render_template("ai.html")

@app.route('/aiform' , methods=['GET' , 'POST'])
def aiform():
    return render_template("aiform.html")


#simple pages routes
#easter egg route(found on how to play section on home page)
@app.route('/easter')
def easter():
    return render_template("easter.html")


#play menu route
@app.route('/play')
def playmenu():
    return render_template("playmenu.html")


#home page route
@app.route('/')
def home():
    return render_template("home.html")
if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')

