import sqlite3

con = sqlite3.connect("../ProjectMgmt.db")
cur = con.cursor()

# 查詢資料
ret = cur.execute("SELECT * FROM Todo")
row = ret.fetchall()

print(row)

con.close()