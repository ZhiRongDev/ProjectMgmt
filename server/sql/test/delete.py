import sqlite3

con = sqlite3.connect("../ProjectMgmt.db")
cur = con.cursor()

cur.execute("DELETE FROM Task_Card")

con.commit()
con.close()