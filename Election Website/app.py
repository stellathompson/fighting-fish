'''
    main-website.py

    Stella Thompson, Kritika Pandit, Luha Yang, Daniel Lumbu, Yeseo Jeon
    March 4, 2024

    Flask API to support Election Data Visualizer web application
    that uses 2016 and 2020 election database.
'''


import psycopg2
import os
import webbrowser
from flask import Flask, render_template
import math
from threading import Timer

import time

app = Flask(__name__)

# To test hompage
# http://stearns.mathcs.carleton.edu:<port number>/


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


    return render_template("select-county-page.html",  counties = list_of_counties, state = state )

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
    # getting the 2016 results for the state and county
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
    return render_template("index.html", votesdiv = percentages, dermo= percentages2)




# Route to show top 10 states with highest vote percentile for each candidate in each year
@app.route('/top_states', methods=['GET'])
def top_states_page():
    return render_template('top-states-page.html')

@app.route('/api/top_states/<year>', methods=['GET'])
def get_top_states_data(year):
    candidate = name+str(int(year)-2000)
    sql = f"SELECT state, state_code, {candidate} FROM election_state ORDER BY {candidate} DESC LIMIT 5;"
    election_data = get_data(sql)
    return jsonify(election_data)
    

def open_browser(website):
    webbrowser.open_new(website)

if __name__ == '__main__':
    my_port = input("Enter your port number: ")
    website = "stearns.mathcs.carleton.edu:" + my_port + "/"

    Timer(1, open_browser, [website]).start()
    app.run(host='0.0.0.0', port=my_port)