import sqlite3


#connect to sqlite database
conn=sqlite3.connect("CDDatabase3")
#create cursor object
c = conn.cursor()

#delete the content of the table
c.execute('DELETE FROM Cohorts')
conn.commit()

#delete the content of the table
c.execute('DELETE FROM Learners')
conn.commit()

#delete the content of the table
c.execute('DELETE FROM Learners1')
conn.commit()
