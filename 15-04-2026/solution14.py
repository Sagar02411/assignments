
# Q14 (Medium) – SQL + Python DB Connection
import sqlite3

def create_and_insert():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    table_creation_query = """
    CREATE TABLE Students (
        ID INT,
        Name VARCHAR(25),
    );
    """
# Execute the table creation query
    cursor.execute(table_creation_query)
    cursor.execute("INSERT INTO STUDENT VALUES (1,'A')")
    conn.commit()
    conn.close()