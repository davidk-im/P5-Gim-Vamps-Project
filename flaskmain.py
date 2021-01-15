from flask import Flask, render_template

app = Flask(__name__)


#home page route
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/play')
def playmenu():
    return render_template("playmenu.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/playai')
def playai():
    return render_template("ai.html")

@app.route('/howtoplay')
def howtoplay():
    return render_template("howtoplay.html")
if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')

