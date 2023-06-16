import sqlite3
import datetime

con = sqlite3.connect("../ProjectMgmt.db")
cur = con.cursor()

cur.execute("""
    INSERT INTO Task_Card VALUES
        (?, ?, ?, ?, ?, ?, ?)
""", (('54321', 'Card1', 'Card1 text', datetime.date.today(), datetime.date.today(), False, '77889')))

con.commit()
con.close()