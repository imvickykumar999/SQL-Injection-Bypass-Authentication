
# importing module
import sqlite3
 
# connecting to the database
conn = sqlite3.connect("gfg.db")
 
# cursor
crsr = conn.cursor()
 
'''
sqlite3.IntegrityError: UNIQUE constraint failed: emp.staff_number
pk = [2, 3, 4, 5, 6]
replace numbers in pk, as primary keys are unique.
pk = [7,8,9,10,11]
'''

# primary key
# pk = [2, 3, 4, 5, 6]
pk = [7,8,9,10,11]
 
# Enter 5 students first names
f_name = ['Nikhil', 'Nisha', 'Abhinav', 'Raju', 'Anshul']
 
# Enter 5 students last names
l_name = ['Aggarwal', 'Rawat', 'Tomar', 'Kumar', 'Aggarwal']
 
# Enter their gender respectively
gender = ['M', 'F', 'M', 'M', 'F']
 
# Enter their joining data respectively
date = ['2019-08-24', '2020-01-01', '2018-05-14', '2015-02-02', '2018-05-14']
 
for i in range(5):
    # This is the q-mark style:
    crsr.execute(f'INSERT INTO emp VALUES ({pk[i]}, "{f_name[i]}", "{l_name[i]}", "{gender[i]}", "{date[i]}")')
 

# SQL command to insert the data in the table
sql_command = """
INSERT INTO emp VALUES (1, "Rishabh", "Bansal", "M", "2014-03-28");
"""
crsr.execute(sql_command)
 
# another SQL command to insert the data in the table
sql_command = """
INSERT INTO emp VALUES (12, "Bill", "Gates", "M", "1980-10-28");
"""
crsr.execute(sql_command)


# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
conn.commit()
 
# close the connection
conn.close()
