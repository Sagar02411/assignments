# Q14 (Medium) – SQL + Python DB Connection
import sqlite3

def create_and_insert():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    Creating_table ="""CREATE TABLE STUDENTS(
    id int PRIMARYKEY
    name VARCHAR(255);
    )"""
    INSERT_QUERY = """INSERT INTO students ('id', 'name') VALUES (1,'Devansh'); """
    # Create table students(id, name)
    # Insert 2 records
    
    conn.commit()
    conn.close()