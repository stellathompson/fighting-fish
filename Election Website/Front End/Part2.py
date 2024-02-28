import psycopg2
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    bodyText= "Welcome to my website! Click on the button below for a surprise!"
    return render_template("homepage.html", bodyText = bodyText )

@app.route('/pop/<word1>')
def counties(word1):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lumbud",
        user="lumbud",
        password="spider665eyebrow")

    cur = conn.cursor()
    state_name = word1.upper()
    sql = f"SELECT county FROM elections WHERE state = '{state_name}';"
    cur.execute(sql)
    list_of_counties = cur.fetchall()


    return render_template("back.html",  counties = list_of_counties)


if __name__ == '__main__':
    my_port = 5129
    app.run(host='0.0.0.0', port = my_port)
