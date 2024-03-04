
# /*
#  * piecharts.py
#  * Author: Kritika Pandit
# THIS FILE HAS A LOT OF ERRORS,
# I WAS JUST TTRYING DIFFERNT IDEAS AND LOOKING OVER IF IT WORKS:
#  */


import psycopg2


# This function tests to make sure that you can connect to the database
def test_connection():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    dropsql = """DROP TABLE IF EXISTS elections;"""

    electionssql = """
    CREATE TABLE elections 
    (county text, state text, trump16 float, clinton16 float, totalvote16 int,
    trump20 float, biden20 float, totalvote20 int, cases int, deaths int, totalpop int, 
    men int, women int, hispanic float, white float, black float, native float,
    asian float, pacific float, poverty float );
    """

    cur = conn.cursor()

    cur.execute(dropsql)
    cur.execute( electionssql )

    conn.commit()
    county_name = input("Enter the name of the county: ")

# Example SQL query to extract data for demographics and voting results for the chosen county
    query = """
    SELECT hispanic, white, black, native, asian, pacific, trump16, clinton16, trump20, biden20
    FROM elections
    WHERE county = ?
    """

    cursor.execute(query, (county_name,))
    data = cursor.fetchone()

#  using the sql queeries made:
if data:
    demographics_data = {
        'Hispanic': data[0],
        'White': data[1],
        'Black': data[2],
        'Native': data[3],
        'Asian': data[4],
        'Pacific': data[5],
    }

    voting_results_data = {
        'Trump 2016': data[6],
        'Clinton 2016': data[7],
        'Trump 2020': data[9],
        'Biden 2020': data[10],
    }

# If there is any null, if the county is not found, then:
else:
    print("County not found.")
