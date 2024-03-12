# Flask API to support Election Data Visualizer web application
# that uses 2016 and 2020 election database.
#
# author: Stella Thompson, Kritika Pandit, Luha Yang, Daniel Lumbu, Yeseo Jeon
# Feb 2024

import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

# To test hompage
# http://stearns.mathcs.carleton.edu:5137/
@app.route('/')
def load_homepage():
    return render_template("homepage.html")

def get_data(sql):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")
    
    cur = conn.cursor()
    cur.execute(sql)

    data = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()

    return data

@app.route('/state/<state>')
def load_select_county_page(state):

    state_name = state.upper()
    sql = f"SELECT county FROM elections WHERE state = '{state_name}';"
    list_of_counties = get_data(sql)

    return render_template("select-county-page.html",  counties = list_of_counties, state = state )

@app.route('/aboutus')
def load_aboutus_page():
    return render_template("about-us-page.html")

@app.route('/results/<state>/<county>/<year>')
def load_results_page(county, state, year):

    if year == '2016':
        candidate_rep = 'trump16'
        candidate_dem = 'clinton16'
        candidate_name = 'Clinton'
    else:
        candidate_rep = 'trump20'
        candidate_dem = 'biden20'
        candidate_name = 'Biden'

    # Getting the 2016 vote results for the selected county
    sql1 = f"SELECT {candidate_rep}, {candidate_dem} FROM elections WHERE county = '{county}' AND state = '{state}';"
    vote_results = get_data(sql1)

    # Calculating percentages
    percentages_vote = calculate_vote_percentages(vote_results)
    
    # Getting dermographics for the selected state
    sql2 = f"SELECT hispanic, white, black, native, asian, pacific FROM elections WHERE county = '{county}' AND state = '{state}';"
    demographics = get_data(sql2)

    # Calculating percentages
    percentages_pop = calculate_demographics_percentages(demographics)
    
    return render_template("results-page.html", votesdiv = percentages_vote, demo= percentages_pop, candidate_name = candidate_name)

def calculate_vote_percentages(vote_results):
    # Given numbers
    candidate_rep = vote_results[0][0]
    candidate_dem = vote_results[0][1]

    # Calculate the total
    total_vote = candidate_rep + candidate_dem

    # Calculate the percentages
    candidate_rep_percentage = (candidate_rep / total_vote) * 100
    candidate_dem_percentage = (candidate_dem / total_vote) * 100

    percentages_vote = [round(candidate_rep_percentage),round(candidate_dem_percentage)]
    return percentages_vote
    
def calculate_demographics_percentages(demographics):
    hispanic = demographics[0][0]
    white = demographics[0][1]
    black = demographics[0][2]
    native = demographics[0][3]
    asian = demographics[0][4]
    pacific = demographics[0][5]

    total_pop = hispanic + white + black + native + asian + pacific

    hispanic_percentage = (hispanic / total_pop) * 100
    white_percentage = (white / total_pop) * 100
    black_percentage = (black / total_pop) * 100
    native_percentage = (native / total_pop) * 100
    asian_percentage = (asian / total_pop) * 100
    pacific_percentage = (pacific / total_pop) * 100

    percentages_pop =[hispanic_percentage, white_percentage, black_percentage, native_percentage, asian_percentage, pacific_percentage]
    
    return percentages_pop

'''
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
'''

if __name__ == '__main__':
    # my_port = 5137
    # print("Open the web browser using port number: " + my_port + ".")

    my_port = input("Enter your port number: ")
    print("Open the web browser using your port number.")

    print("Here's the link:")
    url = "http://stearns.mathcs.carleton.edu:{}/".format(my_port)
    print(url)

    app.run(host='0.0.0.0', port=my_port, debug=False)
