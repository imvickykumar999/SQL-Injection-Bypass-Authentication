
import sqlite3
 
# connecting to the database
conn = sqlite3.connect("myDB.db")
 
# cursor
crsr = conn.cursor()
 
'''
sqlite3.OperationalError: table emp already exists
CREATE TABLE IF NOT EXISTS emp
'''

# SQL command to create a table in the database
sql_command = """
CREATE TABLE IF NOT EXISTS emp (
staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR(1),
joining DATE);
"""

# execute the statement
crsr.execute(sql_command)
 
# close the connection
conn.close()
