# What is in this file: API for fighting-fish
#
# author: Luha Yang
#


from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from operator import itemgetter

app = Flask(__name__, 
        static_url_path='',
        static_folder='static',
        template_folder='templates')

# To test hompage
# http://stearns.mathcs.carleton.edu:5137/
@app.route('/')
def load_hompage():
    return render_template('homepage.html')

@app.route('/pop/<state>')
def counties(state):
    state_name = state.upper()
    sql = f"SELECT county FROM elections WHERE state = '{state_name}';"
    list_of_counties = list(map(itemgetter(0), get_data(sql)))
    return list_of_counties

@app.route('/aboutus')
def aboutus_page():
    return render_template("about-us-page.html")

@app.route('/results/<state>/<county>/2016')
def load_results_page():
    return render_template("results-page.html")

# This function sends a given sql query to the database
# and returns the data obtained as a list (row) of tuples (cols).
def get_data(sql):
    conn = psycopg2.connect(
        host="localhost", 
        port = 5432, 
        database="panditk", 
        user="panditk", 
        password="square555cow")
    
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

'''
# Candidate-based queries
@app.route('/<year>/<candidate>')
def search_candidate(year, candidate):
    conn = psycopg2.connect(host="localhost", port = 5432, database="panditk", user="panditk", password="square555cow")
    cur = conn.cursor()

    if year == 2016 and candidate == "Trump":
        search = "trump16"
    elif year == 2020 and candidate == "Trump":
        search = "trump20"
    elif year == 2016 and candidate == "Clinton":
        search == "clinton16"
    else:
        search == "biden20"

    search_results = search_database(conn, cur, search)

    cur.close()
    conn.close()

    return render_template('results.html', output = search_results)

# Searh <what> in the database
def search_database(db_conn, db_cursor, search):
    sql_query = "SELECT county, state, {} FROM elections WHERE {} IS NOT NULL ORDER BY {} DESC;".format(search, search, search)

    # When having multiple queries in one line
    sql_query_list = sql_query.split(';')
    for query in sql_query_list:
        if (len(query) > 2):
            db_cursor.execute(query) 
    
    row_list = db_cursor.fetchall()

    db_conn.commit()

    output_str = ""
    for row in row_list:
        output_str = output_str + str(row) + ",   "
        output_str = output_str + "\n"
    
    return output_str
'''


if __name__ == '__main__':
    my_port = 5137
    app.run(host='0.0.0.0', port=my_port)
