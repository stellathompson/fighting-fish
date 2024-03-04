# What is in this file: API for fighting-fish
#
# author: Luha Yang
#

from flask import Flask, render_template, jsonify
import psycopg2
import os

app = Flask(__name__)

# To test hompage
# http://stearns.mathcs.carleton.edu:5137/
@app.route('/')
def load_hompage():
    return render_template('homepage.html')

@app.route('/pop/<state>')
def counties(state):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(current_directory, '../new-dataset/templates/index.html')
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

if __name__ == '__main__':
    my_port = 5137
    app.run(host='0.0.0.0', port=my_port)
