import sqlite3
conn=sqlite3.connect("pms1.db")
c=conn.cursor()
c.execute("""CREATE TABLE pms1(
	password INTEGER,
	username  TEXT,
	project1 TEXT,
	project2 TEXT
	
	
	)""")
conn.commit()
conn.close()