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
import math

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/state/<state>')
def counties(state):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()
    state_name = state.upper()
    sql = f"SELECT county FROM elections WHERE state = '{state_name}' AND trump16 IS NOT NULL AND white IS NOT NULL;"
    cur.execute(sql)
    list_of_counties = cur.fetchall()
    
    cur = conn.cursor()
    sql = f"SELECT state FROM stateabb WHERE abbreviation = '{state_name}';"
    cur.execute(sql)
    state_fullname = cur.fetchone()
    state_fullname = state_fullname[0]


    return render_template("select-county-page.html",  counties = list_of_counties, state = state_name, fullstate = state_fullname )

@app.route('/aboutus')
def aboutus_page():
    return render_template("about-us-page.html")

@app.route('/results/<state>/<county>/<year>')
def results_page(county,state,year):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()
    
    # getting the 2016 results for the state and county
    if '2016' == year:
        sql = f"SELECT trump16, clinton16 FROM elections WHERE county = '{county}' AND state = '{state}';"
        cur.execute(sql)
        trump = cur.fetchall()
    else:
        sql = f"SELECT trump20, biden20 FROM elections WHERE county = '{county}' AND state = '{state}';"
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

    percentages = [round(percentage1),round(percentage2)]
    # getting Dermographics
    sql2 = f"SELECT hispanic, white, black, native, asian, pacific FROM elections WHERE county = '{county}' AND state = '{state}';"
    cur.execute(sql2)
    dermographics = cur.fetchall()
    hispanic = dermographics[0][0]
    white = dermographics[0][1]
    black = dermographics[0][2]
    native = dermographics[0][3]
    asian = dermographics[0][4]
    pacific = dermographics[0][5]

    total2 = hispanic + white + black + native + asian + pacific

    hispanic_percentage = (hispanic / total2) * 100
    white_percentage = (white / total2) * 100
    black_percentage = (black / total2) * 100
    native_percentage = (native / total2) * 100
    asian_percentage = (asian / total2) * 100
    pacific_percentage = (pacific / total2) * 100

    percentages2 =[hispanic_percentage,white_percentage,black_percentage,native_percentage,asian_percentage,pacific_percentage]
    



    return render_template("results-page.html", votesdiv = percentages, demo= percentages2)
if __name__ == '__main__':
    my_port = 5126
    app.run(host='0.0.0.0', port = my_port)
