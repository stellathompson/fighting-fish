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
        print( "Connection Worked! \n" )
    else:
        print( "Problem with Connection. \n" )

    conn.commit()
    conn.close()
    return None
    
# This function prints top 5 counties voted the most for Trump in 2016
def execute_query_one():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    sql = """SELECT county, state, trump16 FROM elections WHERE trump16 IS NOT NULL AND trump16 > 0.75 ORDER BY trump16 DESC LIMIT 5;"""

    cur.execute( sql )

    row_list = cur.fetchall()

    if not row_list:
        print("No counties voted for Trump in 2016 by more than 75%. \n")
    else:
        print("In 2016, top 5 counties that voted the most for Trump are:")
        for row in row_list:
            print("{}, {} voted for Trump by {:.2f}%.".format(row[0], row[1], round(row[2], 4)*100))
    print("")
    
    conn.commit()
    cur.close()
    conn.close()
    return None

# This function determines which county had the highest population, then prints which percentage of votes towards Trump in 2020
def execute_query_two():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    sql = """SELECT county, state, trump20, biden20, totalpop FROM elections WHERE trump20 IS NOT NULL AND biden20 IS NOT NULL AND totalpop IS NOT NULL ORDER BY totalpop DESC;"""
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong... \n")
    else:
        print("In 2020, the county {}, {} had the highest population of {}. \nThey voted for Trump by {:.2f}% and Biden by {:.2f}%.\n".format(row[0], row[1], row[4], round(row[2], 4)*100, round(row[3], 4)*100))
   
    conn.commit()
    cur.close()
    conn.close()
    return None

# This function determines which county had the highest total vote, then prints which percentage of votes towards Trump and Biden in 2020
def execute_query_three():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    sql = """SELECT county, state, trump16, clinton16, totalvote16 FROM elections WHERE trump16 IS NOT NULL AND clinton16 IS NOT NULL AND totalvote16 IS NOT NULL ORDER BY totalvote16 DESC;"""
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...\n")
    else:
        print("In 2016, the county {}, {} voted the most in total number of {}. \nThey voted for Trump by {:.2f}% and Clinton by {:.2f}%.\n ".format(row[0], row[1], row[4], round(row[2], 4)*100, round(row[3], 4)*100))

    conn.commit()
    cur.close()
    conn.close()
    return None  

# This function determines which county had the highest Black population, then prints which percentage of votes towards Trump and Clinton in 2016
def execute_query_four():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    sql = """SELECT county, state, trump16, clinton16, black FROM elections WHERE trump16 IS NOT NULL AND clinton16 IS NOT NULL AND black IS NOT NULL ORDER BY black DESC;"""
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...\n")
    else:
        print("In 2016, the county {}, {} had the highest Black population of {}%. \nThey voted for Trump by {:.2f}% and Clinton by {:.2f}%.\n ".format(row[0], row[1], row[4], round(row[2], 4)*100, round(row[3], 4)*100))

    conn.commit()
    cur.close()
    conn.close()
    return None


# This function prints which county in NY had the lowest votes towards Trump in 2020
def execute_query_five():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    state_input = input("Enter the abbreviation of state you want to look at: ")

    sql = """SELECT county, state, trump20 FROM elections WHERE state = %s AND trump20 IS NOT NULL ORDER BY trump20;"""
    
    cur.execute( sql, [state_input.upper()] )

    row = cur.fetchone()

    if row == None:
        print("You entered wrong state abbreviation. Try again.\n")
    else:
        print("In 2020, the county {} had the lowest number of votes towards Trump in state {} by {:.2f}%. \n ".format(row[0], row[1], round(row[2], 4)*100))

    conn.commit()
    cur.close()
    conn.close()
    return None


test_connection()

# Functions below send an SQL query to the database
execute_query_one()
execute_query_two()
execute_query_three()
execute_query_four()
execute_query_five()
