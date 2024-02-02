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
    (county text, State text, Trump16 float, clinton16 float, totalvotes16 int,
    Trump20 float, Biden20 float, Totalvotes20 int, Cases int, Deaths int, Totalpop int, 
    Men int, Women int, Hispanic float, White float, Black float, Native float,
    Asian float, Pacific float, Poverty float );
    """


    cur = conn.cursor()

    cur.execute(dropsql)
    cur.execute( electionssql )

    conn.commit()

    return None

test_connection()
