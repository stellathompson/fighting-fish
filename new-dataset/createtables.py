# We use the psycopg2 library to help us connec to the Postgres SQL database
# This library is already installed on stearns.mathcs.carleton.edu
import psycopg2

# This function tests to make sure that you can connect to the database
def test_connection():

    conn = psycopg2.connect(
        host="localhost",
        port=5137,
        database="yangl4",
        user="yangl4",
        password="stars929bond")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    # Drop already existing tables
    drop_sql = """DROP TABLE IF EXISTS election_county, election_state, demographic_state;"""

    # SQL queries separated by semicolons
    sql_queries = """
    CREATE TABLE election_county (
        state text, state_code text, county text, 
        trump16 float, clinton16 float, total16 int, 
        trump20 float, biden20 float, total20 int);
    CREATE TABLE election_state (
        state text, state_code text,
        trump16 float, clinton16 float, total16 int,
        trump20 float, biden20 float, total20 int);
    CREATE TABLE demographic_state (
        state_code text, 
        total int, men int, women int,
        hispanic float, white float, black float, native float, asian float, pacific float,
        poverty float);
    """

    # Split the string into a list of individual queries
    queries = sql_queries.split(';')

    cur = conn.cursor()

    cur.execute(drop_sql)
    
    # Execute each query one by one
    for query in queries:
        if query.strip():
            cur.execute(query)
    
    print("Queries executed successfully.")

    conn.commit()
    cur.close()
    conn.close()

    return None

test_connection()
