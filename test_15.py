import sqlite3

def create_connection():
    conn = None
    try:
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')
       
    except Exception as e:
        print(e)
    return conn