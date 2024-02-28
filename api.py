# What is in this file: API for fighting-fish
#
# author: Luha Yang
#


from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__, 
        static_url_path='',
        static_folder='static',
        template_folder='templates')

# To test hompage
# http://stearns.mathcs.carleton.edu:5137/
@app.route('/')
def load_hompage():
    bodyText= "Welcome to my website! Click on the button below for a surprise!"
    return app.send_static_file('hompage.html', bodyText = bodyText)
    
# Candidate-based queries
@app.route('/<year>/<candidate>')
def search_candidate(year, candidate):
    conn = psycopg2.connect(host="localhost", port = 5432, database="yangl4", user="yangl4", password="stars929bond")
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


if __name__ == '__main__':
    my_port = 5137
    app.run(host='0.0.0.0', port=my_port)
