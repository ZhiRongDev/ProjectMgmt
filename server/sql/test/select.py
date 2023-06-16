import sqlite3
import json

con = sqlite3.connect("../ProjectMgmt.db")
cur = con.cursor()

# 查詢資料
ret = cur.execute("SELECT * FROM user")
# print(ret.fetchall())
row = ret.fetchall()

print(row)

# for i in row:
#     print(i[0])

con.close()