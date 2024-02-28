import psycopg2
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/pop/<state>')
def counties(state):
    conn = psycopg2.connect(
        host="localhost",
        port=5129,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()
    state_name = state.upper()
    sql = f"SELECT county FROM elections WHERE state = '{state_name}';"
    cur.execute(sql)
    list_of_counties = cur.fetchall()


    return render_template("back.html",  counties = list_of_counties)

@app.route('/aboutus')
def aboutus_page():
    return render_template("aboutus.html")

if __name__ == '__main__':
    my_port = 5129
    app.run(host='0.0.0.0', port = my_port)
