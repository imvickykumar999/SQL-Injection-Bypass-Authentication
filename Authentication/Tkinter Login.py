
# https://www.geeksforgeeks.org/create-mysql-database-login-page-in-python-using-tkinter/
# https://www.w3schools.com/python/python_mysql_getstarted.asp

'''
Should I use SQLite or MySQL?

MySQL has a well-constructed user management system which can handle 
multiple users and grant various levels of permission. 
SQLite is suitable for smaller databases. 
As the database grows the memory requirement also gets larger while 
using SQLite. Performance optimization is harder when using SQLite.

SQLite is probably the most straightforward database to 
connect to with a Python application since you don't need 
to install any external Python SQL modules to do so.
'''	

import tkinter as tk
import mysql.connector
from tkinter import *


def submitact():
	
	user = Username.get()
	passw = password.get()

	print(f"The name entered by you is {user} {passw}")

	logintodb(user, passw)


def logintodb(user, passw):
	
	# If password is entered by the
	# user
	if passw:
		db = mysql.connector.connect(host ="localhost",
									user = user,
									password = passw,
									db ="College")
		cursor = db.cursor()
		
	# If no password is entered by the
	# user
	else:
		db = mysql.connector.connect(host ="localhost",
									user = user,
									db ="College")
		cursor = db.cursor()
		
	# A Table in the database
	savequery = "select * from STUDENT"
	
	try:
		cursor.execute(savequery)
		myresult = cursor.fetchall()
		
		# Printing the result of the
		# query
		for x in myresult:
			print(x)
		print("Query Executed successfully")
		
	except:
		db.rollback()
		print("Error occurred")


root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")


# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)

lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)

password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Login",
					bg ='yellow', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)

root.mainloop()
