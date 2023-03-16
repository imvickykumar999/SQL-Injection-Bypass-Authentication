import sqlite3 as sql

con = sql.connect("database.db", check_same_thread=False)
with con as f:
    f.execute(open("schema.sql", "r").read())

def insertUser(username,password):
    cur = con.cursor()
    cur.execute(f"INSERT INTO users VALUES (?,?)", ({username},{password}))
    con.commit()
    con.close()

def retrieveUsers():
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users
