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

    sql = " SELECT * FROM elections ORDER BY deaths DESC "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print(row[0], "had the most COVID deaths in 2020 and voted Trump", row[2], "and Biden", row[3])

    conn.commit()

# def test_query_three():

#     conn = psycopg2.connect(
#         host="localhost",
#         port=5432,
        # database="panditk",
        # user="panditk",
        # password="square555cow")

#     cur = conn.cursor()

#     sql = " SELECT * FROM cities WHERE state = 'Minnesota' ORDER BY population ASC "
    
#     cur.execute( sql )

#     row = cur.fetchone()

#     if row == None:
#         print("Something went wrong...")
#     else:
#         print(row[0], "has a population of", row[2], "(the smallest in Minnesota).")

#     conn.commit()

# def test_query_four():

#     conn = psycopg2.connect(
#         host="localhost",
#         port=5432,
        # database="panditk",
        # user="panditk",
        # password="square555cow")

#     cur = conn.cursor()

# #North
#     sql = " SELECT * FROM cities ORDER BY lat DESC "
    
#     cur.execute( sql )

#     row = cur.fetchone()

#     if row == None:
#         print("Something went wrong...")
#     else:
#         print(row[0], "is furthest North.")

# #South
#     sql = " SELECT * FROM cities ORDER BY lat ASC "
    
#     cur.execute( sql )

#     row = cur.fetchone()

#     if row == None:
#         print("Something went wrong...")
#     else:
#         print(row[0], "is furthest South.")    

# #East
#     sql = " SELECT * FROM cities ORDER BY lon DESC "
    
#     cur.execute( sql )

#     row = cur.fetchone()

#     if row == None:
#         print("Something went wrong...")
#     else:
#         print(row[0], "is farthest East.")

# #West
#     sql = " SELECT * FROM cities ORDER BY lon ASC "
    
#     cur.execute( sql )

#     row = cur.fetchone()

#     if row == None:
#         print("Something went wrong...")
#     else:
#         print(row[0], "is farthest West.")
        
#     conn.commit()
    

# def test_query_five():

#     conn = psycopg2.connect(
#         host="localhost",
#         port=5432,
        # database="panditk",
        # user="panditk",
        # password="square555cow")

#     cur = conn.cursor()
#     state = input("What is the name of the state you are looking for?")
    
#     if len(state) == 2:
#         sql = "SELECT * FROM abbreviations WHERE abbreviation = '" + state + "'"
#         cur.execute(sql)
#         row = cur.fetchone()
#         state_name = row[0]
#     else:
#         state_name = state

#     #if length of string is 2, then go to abbreviation table and find the state
#     #turn the state into variable that is then used in the SQL call
#     #else, put the state directly into the SQL command
#     sql = " SELECT * FROM cities WHERE state = '" + state_name + "'"
    
#     cur.execute( sql )

#     rows = cur.fetchall()
#     total_population = 0
#     for row in rows:
#         total_population += row[2]


#     if row == None:
#         print("Something went wrong...")
#     else:
#         print("Total population of", state_name, "is", total_population)

#     conn.commit()

test_connection()
test_query_one()
