# api.py
# author: Kritika Pandit
#This is little try out version for the app route, i used api that luha made.
#
from operator import itemgetter

import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

# To test hompage
# http://stearns.mathcs.carleton.edu:5131/

# This is API for Piecharts:
@app.route('/piecharts/<state>/<county>/2016')
def load_results_page():
    return render_template("piecharts.html")


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


if __name__ == '__main__':
    my_port = 5137
    app.run(host='0.0.0.0', port=my_port)
