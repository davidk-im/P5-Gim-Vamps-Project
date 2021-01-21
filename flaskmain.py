from flask import Flask, render_template, request
from user import user_create
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

''' database setup  '''
dbURI = 'sqlite:///chess.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)
db.init_app(app)


#home page route
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/play')
def playmenu():
    return render_template("playmenu.html")

@app.route('/signup' ,methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['password']
        user_create(username, password)
        return render_template("signconfirm.html")
    else:
        print('Bar')
    return render_template("signup.html")

@app.route('/playai')
def playai():
    return render_template("ai.html")

@app.route("/playai", methods=['GET','POST'])
def createBoardTable():
    if request.method == 'POST':
        form = request.form
        movelist.clear()
        board = og_board
        storeboard = ogstoreboard
        return render_template("playai.html", displayClicked="  ", allBoard=chessData.split_board(board))


@app.route('/signinsuccess')
def signconfirm():
    return render_template("signconfirm.html")

@app.route('/howtoplay')
def howtoplay():
    return render_template("howtoplay.html")

@app.route('/leaderboards')
def leaderboards():
    return render_template("leaderboards.html")

if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')

