# We use the psycopg2 library to help us connec to the Postgres SQL database
# This library is already installed on stearns.mathcs.carleton.edu
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

    dropsql = """ DROP TABLE IF EXISTS elections; """

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

    return None

test_connection()
