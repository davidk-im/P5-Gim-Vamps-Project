from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#home page route
@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')