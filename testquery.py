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

    return None

def test_query_one():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    sql = "SELECT * FROM elections WHERE Trump16 > 0.75 ORDER BY Trump16 DESC"
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("No counties voted for Trump in 2016 by more than 75%")
    else:
        print("The county that voted the most for Trump in 2016 is", row[0], "by", row[2])

    conn.commit()

def test_query_two():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    sql = " SELECT * FROM elections WHERE Totalpop IS NOT null ORDER BY Totalpop DESC "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print(row[0], "county had the highest population in 2020 and voted Trump", row[5], "and Biden", row[6])

    conn.commit()

def test_query_three():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    sql = "SELECT * FROM elections ORDER BY totalvotes16"
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print("The county with the most total votes in 2016 is", row[0], "and they voted for Clinton by", row[3])

    conn.commit()
    

def test_query_four():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    sql = " SELECT * FROM elections ORDER BY Black DESC"
    
    cur.execute( sql )

    row = cur.fetchone()


    if row == None:
        print("Something went wrong...")
    else:
        print("The county with the highest percentage of Black people voted for Trump", row[2], "and Clinton", row[3], "in 2016.")

    conn.commit()

test_connection()
test_query_one()
test_query_two()
test_query_three()
test_query_four()