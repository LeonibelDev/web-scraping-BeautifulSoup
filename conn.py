import sqlite3

conn = sqlite3.connect("./db/database.db")
c = conn.cursor()

def execute_query(query):
    c.execute(query)
    conn.commit()
    return c