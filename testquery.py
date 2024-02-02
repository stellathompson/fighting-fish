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

    conn.commit()
    conn.close()
    return None

def test_query_one():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    #sql = """SELECT county, state, trump16 FROM elections WHERE trump16 > 0.75 ORDER BY trump16 DESC;"""
    sql = """SELECT county, state, trump16 FROM elections ORDER BY trump16 DESC;"""

    cur.execute( sql )

    # row = cur.fetchone()

    #test
    row = cur.fetchall()
    for r in row:
        print (r)

    '''if row == None:
        print("No counties voted for Trump in 2016 by more than 75%")
    else:
        print("The county {}, {} voted the most for Trump in 2016 by {:.2f}%.".format(row[0], row[1], round(row[2], 2)*100))
    '''
    conn.commit()

def test_query_two():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    sql = " SELECT * FROM elections WHERE totalpop IS NOT null ORDER BY totalpop DESC "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print(row[0], "county had the highest population in 2020 and voted Trump by", row[5], "and Biden by", row[6])

    conn.commit()

def test_query_three():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    sql = "SELECT * FROM elections WHERE totalvote16 IS NOT null ORDER BY totalvote16 DESC"
    
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

    sql = " SELECT * FROM elections WHERE trump16 IS NOT null AND clinton16 IS NOT null ORDER BY black DESC"
    
    cur.execute( sql )

    row = cur.fetchone()


    if row == None:
        print("Something went wrong...")
    else:
        print("The county with the highest percentage of Black people voted for Trump", row[2], "and Clinton", row[3], "in 2016.")

    conn.commit()

def test_query_five():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    sql = " SELECT * FROM elections WHERE state = 'NY' ORDER BY trump20 ASC "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong, try again")
    else:
        print( " The county", row[0],"had the lowest number of votes towards Trump in New York by", row[2])

    conn.commit()


test_connection()
test_query_one()
'''test_query_two()
test_query_three()
test_query_four()
test_query_five()'''
