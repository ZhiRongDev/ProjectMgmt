import sqlite3

con = sqlite3.connect("../ProjectMgmt.db")
cur = con.cursor()

cur.execute("DELETE FROM Task_List")

con.commit()
con.close()