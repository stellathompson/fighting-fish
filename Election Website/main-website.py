'''
    main-website.py

    Stella Thompson, Kritika Pandit, Luha Yang, Daniel Lumbu, Yeseo Jeon
    March 4, 2024

    Flask API to support Election Data Visualizer web application
    that uses 2016 and 2020 election database.
'''


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
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()
    state_name = state.upper()
    sql = f"SELECT county FROM elections WHERE state = '{state_name}';"
    cur.execute(sql)
    list_of_counties = cur.fetchall()


    return render_template("select-county-page.html",  counties = list_of_counties,state = state )

@app.route('/aboutus')
def aboutus_page():
    return render_template("about-us-page.html")

@app.route('/results/<state>/<county>/2016')
def results_page(county,state):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()
    sql = f"SELECT trump16, clinton16 FROM elections WHERE county = '{county}' AND state = '{state}';"
    cur.execute(sql)
    trump = cur.fetchall()

    # Given numbers
    number1 = trump[0][0]
    number2 = trump[0][1]

    # Calculate the total
    total = number1 + number2

    # Calculate the percentages
    percentage1 = (number1 / total) * 100
    percentage2 = (number2 / total) * 100

    percentages = [percentage1,percentage2]

    return render_template("index.html", votesdiv = percentages)
if __name__ == '__main__':
    my_port = 5126
    app.run(host='0.0.0.0', port = my_port)




    

