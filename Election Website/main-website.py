'''
    main-website.py

    Yeseo Jeon, Stella Thompson, Kritika Pandit, Luha Yang, Daniel Lumbu
    March 4, 2024

    Flask API to support Election Data Visualizer web application
    that uses 2016 and 2020 election database.
'''


import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/pop/<state>')
def counties(state):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()
    state_name = state.upper()
    sql = f"SELECT county FROM elections WHERE state = '{state_name}';"
    cur.execute(sql)
    list_of_counties = cur.fetchall()


    return render_template("select-county-page.html",  counties = list_of_counties)

@app.route('/aboutus')
def aboutus_page():
    return render_template("about-us-page.html")

@app.route('/results/<county>/2016')
def results_page(county):
    return render_template("results-page.html", countyname = county)

if __name__ == '__main__':
    my_port = 5129
    app.run(host='0.0.0.0', port = my_port)
