import sqlite3
import datetime

con = sqlite3.connect("../ProjectMgmt.db")
cur = con.cursor()

# cur.execute("""
#     INSERT INTO Task_Card VALUES
#         (?, ?, ?, ?, ?, ?, ?)
# """, (('54321', 'Card1', 'Card1 text', datetime.date.today(), datetime.date.today(), False, '77889')))

cur.execute("""
    INSERT INTO user VALUES
        (?, ?, ?, ?, ?)
""", (('123', 'jordan', 'jordan@gmail.com', 'https://randomuser.me/api/portraits/men/1.jpg', '123')))


con.commit()
con.close()