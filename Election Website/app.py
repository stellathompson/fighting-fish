# What is in this file: API for fighting-fish
#
# author: Luha Yang
#

from flask import Flask, render_template, jsonify
import psycopg2
import os
import webbrowser

app = Flask(__name__)

# To test hompage
# http://stearns.mathcs.carleton.edu:<port number>/
@app.route('/')
def load_hompage():
    return render_template('homepage.html')

@app.route('/pop/<state>')
def counties(state):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(current_directory, '/piechart/templates/index.html')
    return render_template(template_path)

@app.route('/aboutus')
def aboutus_page():
    return render_template("about-us-page.html")

@app.route('/results/<state>/<county>/2016')
def load_results_page():
    return render_template("results-page.html")

# This function sends a given sql query to the database
# and returns the data obtained as a list (row) of tuples (cols).
def get_data(query):
    conn = psycopg2.connect(
        host="localhost", 
        port = 5137, 
        database="yangl4", 
        user="yangl4", 
        password="stars929bond")
    
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()

@app.route('/api/pie_data/<state>', methods=['GET'])
def get_pie_data(state):
    sql = f"SELECT * FROM election_county WHERE state_code = '{state.upper()}';"
    data = get_data(sql)
    return jsonify(data)

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


if __name__ == '__main__':
    my_port = input("Enter your port number")
    app.run(host='0.0.0.0', port=my_port)
    website = "http://stearns.mathcs.carleton.edu:" + my_port + "/"
    webbrowser.open(website)
