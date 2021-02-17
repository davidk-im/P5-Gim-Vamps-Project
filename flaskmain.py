from flask import (Flask, g, redirect, render_template, request, session, url_for)
from user import user_create
from flask_sqlalchemy import SQLAlchemy
import requests
import chessdata
from chessdata import board, movelist, og_board, ogstoreboard
from markupsafe import escape
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from user import validate_user, User


app = Flask(__name__)


# database setup
dbURI = 'sqlite:///chess.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)
db.init_app(app)

app.config['SECRET_KEY'] = '1234'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        #username and password variables from form
        username = request.form['Username']
        password = request.form['password']
        #just to check if username and password was collected
        print(username +" " + password)
        #calls validate_user function from user.py
        user=validate_user(username, password)
        if user:
            #if validate_user = true, log user in and return profile.html template
            login_user(user)
            return render_template("profile.html")
    else:
        print('Bar')
        #if validate_user = false, return login page
    return render_template("login.html")


#route for profile page
#@login_required tag used to ensure that user cannot access profile if not signed in
@app.route('/profile')
@login_required
def dashboard():
    return render_template('profile.html', name=current_user.username)

#route for logging out
#@login_required tag used to ensure that user must be logged in to log out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.html'))

#home page route
@app.route('/')
def home():
    return render_template("home.html")

#play menu route
@app.route('/play')
def playmenu():
    return render_template("playmenu.html")

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
    else:
        print('Bar')
        #if for some reason form doesn't go through for some reason, returns signup page again
    return render_template("signup.html")

#sign up success page returned after post process above
@app.route('/signupsuccess')
def signconfirm():
    return render_template("signconfirm.html")

@app.route('/chessdicttable')
def chessdicttable():
    return render_template("chessdicttable.html")

#main ai chess game route
@app.route('/playai')
def playai():
    return render_template("ai.html")

#easter egg route(found on how to play section on home page)
@app.route('/easter')
def easter():
    return render_template("easter.html")

#route to test chess game
@app.route('/testchess')
def testchess():
    return render_template("testchess.html")

#chess offline website leaderboards
@app.route('/leaderboards')
def leaderboards():
    return render_template("leaderboards.html")

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
        storeboard = ogstoreboard #resets the storboard
        return render_template("chessDictTable.html", displayClicked="  ", allBoard=chessdata.split_board(board))
"""    return redirect("/project/chessDictTable/") #redirects to format into the chess board"""

@app.route("/a8", methods=['GET','POST'])#-------------------------------------------------------------------------------------this is where it starts
def a8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a8", movelist=chessdata.movesdata("a8"), message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/a7", methods=['GET','POST'])
def a7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a7", movelist=chessdata.movesdata("a7"),  message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))

@app.route("/a6", methods=['GET','POST'])
def a6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a6", movelist=chessdata.movesdata("a6"),  message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/a5", methods=['GET','POST'])
def a5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a5", movelist=chessdata.movesdata("a5"),  message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/a4", methods=['GET','POST'])
def a4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a4" , movelist=chessdata.movesdata("a4"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/a3", methods=['GET','POST'])
def a3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a3" , movelist=chessdata.movesdata("a3"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/a2", methods=['GET','POST'])
def a2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a2" , movelist=chessdata.movesdata("a2"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/a1", methods=['GET','POST'])
def a1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="a1" , movelist=chessdata.movesdata("a1"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/b8", methods=['GET','POST'])
def b8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b8" , movelist=chessdata.movesdata("b8"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/b7", methods=['GET','POST'])
def b7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b7" , movelist=chessdata.movesdata("b7"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/b6", methods=['GET','POST'])
def b6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b6" , movelist=chessdata.movesdata("b6"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/b5", methods=['GET','POST'])
def b5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b5" , movelist=chessdata.movesdata("b5"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/b4", methods=['GET','POST'])
def b4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b4" , movelist=chessdata.movesdata("b4"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/b3", methods=['GET','POST'])
def b3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b3" , movelist=chessdata.movesdata("b3"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/b2", methods=['GET','POST'])
def b2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b2" , movelist=chessdata.movesdata("b2"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/b1", methods=['GET','POST'])
def b1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="b1" , movelist=chessdata.movesdata("b1"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))

@app.route("/c8", methods=['GET','POST'])
def c8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c8" , movelist=chessdata.movesdata("c8"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/c7", methods=['GET','POST'])
def c7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c7" , movelist=chessdata.movesdata("c7"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/c6", methods=['GET','POST'])
def c6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c6" , movelist=chessdata.movesdata("c6"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/c5", methods=['GET','POST'])
def c5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c5" , movelist=chessdata.movesdata("c5"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/c4", methods=['GET','POST'])
def c4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c4" , movelist=chessdata.movesdata("c4"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/c3", methods=['GET','POST'])
def c3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c3" , movelist=chessdata.movesdata("c3"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/c2", methods=['GET','POST'])
def c2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c2" , movelist=chessdata.movesdata("c2"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/c1", methods=['GET','POST'])
def c1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="c1" , movelist=chessdata.movesdata("c1"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))

@app.route("/d8", methods=['GET','POST'])
def d8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d8" , movelist=chessdata.movesdata("d8"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/d7", methods=['GET','POST'])
def d7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d7" , movelist=chessdata.movesdata("d7"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/d6", methods=['GET','POST'])
def d6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d6" , movelist=chessdata.movesdata("d6"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/d5", methods=['GET','POST'])
def d5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d5" , movelist=chessdata.movesdata("d5"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/d4", methods=['GET','POST'])
def d4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d4" , movelist=chessdata.movesdata("d4"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/d3", methods=['GET','POST'])
def d3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d3" , movelist=chessdata.movesdata("d3"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/d2", methods=['GET','POST'])
def d2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d2" , movelist=chessdata.movesdata("d2"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/d1", methods=['GET','POST'])
def d1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="d1" , movelist=chessdata.movesdata("d1"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))

@app.route("/e8", methods=['GET','POST'])
def e8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e8" , movelist=chessdata.movesdata("e8"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/e7", methods=['GET','POST'])
def e7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e7" , movelist=chessdata.movesdata("e7"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/e6", methods=['GET','POST'])
def e6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e6" , movelist=chessdata.movesdata("e6"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/e5", methods=['GET','POST'])
def e5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e5" , movelist=chessdata.movesdata("e5"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/e4", methods=['GET','POST'])
def e4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e4" , movelist=chessdata.movesdata("e4"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/e3", methods=['GET','POST'])
def e3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e3" , movelist=chessdata.movesdata("e3"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/e2", methods=['GET','POST'])
def e2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e2" , movelist=chessdata.movesdata("e2"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/e1", methods=['GET','POST'])
def e1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="e1" , movelist=chessdata.movesdata("e1"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))

@app.route("/f8", methods=['GET','POST'])
def f8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f8" , movelist=chessdata.movesdata("f8"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/f7", methods=['GET','POST'])
def f7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f7" , movelist=chessdata.movesdata("f7"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/f6", methods=['GET','POST'])
def f6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f6" , movelist=chessdata.movesdata("f6"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/f5", methods=['GET','POST'])
def f5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f5" , movelist=chessdata.movesdata("f5"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/f4", methods=['GET','POST'])
def f4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f4" , movelist=chessdata.movesdata("f4"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/f3", methods=['GET','POST'])
def f3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f3" , movelist=chessdata.movesdata("f3"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/f2", methods=['GET','POST'])
def f2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f2" , movelist=chessdata.movesdata("f2"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/f1", methods=['GET','POST'])
def f1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="f1" , movelist=chessdata.movesdata("f1"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))

@app.route("/g8", methods=['GET','POST'])
def g8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g8" , movelist=chessdata.movesdata("g8"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/g7", methods=['GET','POST'])
def g7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g7" , movelist=chessdata.movesdata("g7"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/g6", methods=['GET','POST'])
def g6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g6" , movelist=chessdata.movesdata("g6"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/g5", methods=['GET','POST'])
def g5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g5" , movelist=chessdata.movesdata("g5"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/g4", methods=['GET','POST'])
def g4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g4" , movelist=chessdata.movesdata("g4"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/g3", methods=['GET','POST'])
def g3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g3" , movelist=chessdata.movesdata("g3"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/g2", methods=['GET','POST'])
def g2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g2" , movelist=chessdata.movesdata("g2"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/g1", methods=['GET','POST'])
def g1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="g1" , movelist=chessdata.movesdata("g1"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))

@app.route("/h8", methods=['GET','POST'])
def h8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h8" , movelist=chessdata.movesdata("h8"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/h7", methods=['GET','POST'])
def h7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h7" , movelist=chessdata.movesdata("h7"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/h6", methods=['GET','POST'])
def h6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h6" , movelist=chessdata.movesdata("h6"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/h5", methods=['GET','POST'])
def h5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h5" , movelist=chessdata.movesdata("h5"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/h4", methods=['GET','POST'])
def h4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h4" , movelist=chessdata.movesdata("h4"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/h3", methods=['GET','POST'])
def h3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h3" , movelist=chessdata.movesdata("h3"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/h2", methods=['GET','POST'])
def h2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h2" , movelist=chessdata.movesdata("h2"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))
@app.route("/h1", methods=['GET','POST'])
def h1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked="h1" , movelist=chessdata.movesdata("h1"),   message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))


if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')

