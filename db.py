import sqlite3

conn = sqlite3.connect("staffs.sqllite")


cursor = conn.cursor()
sql_query = """CREATE TABLE staff (
    id integer PRIMARY KEY,
    user text NOT NULL,
    number text NOT NULL
)"""

cursor.execute(sql_query)
