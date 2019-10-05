import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

conn = create_connection("mynew.db") 

c = conn.cursor()

sqlT = "SELECT * FROM tasks;"
r = c.execute(sqlT)
for x in r: print(x)

sqlP = "SELECT * FROM projects;"
r = c.execute(sqlP)
for x in r: print(x)


