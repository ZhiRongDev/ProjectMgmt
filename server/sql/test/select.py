import sqlite3

con = sqlite3.connect("../ProjectMgmt.db")
cur = con.cursor()

# 查詢資料
ret = cur.execute("SELECT * FROM Task_Card")
row = ret.fetchall()

print(row)

con.close()