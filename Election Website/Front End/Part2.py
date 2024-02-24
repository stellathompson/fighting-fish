from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    bodyText= "Welcome to my website! Click on the button below for a surprise!"
    return render_template("homepage.html", bodyText = bodyText )

if __name__ == '__main__':
    my_port = 5126
    app.run(host='0.0.0.0', port = my_port) 