import sqlite3

con = sqlite3.connect("../ProjectMgmt.db")
cur = con.cursor()

cur.execute("DELETE FROM comment")

con.commit()
con.close()