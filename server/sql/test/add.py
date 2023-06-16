import sqlite3

con = sqlite3.connect("../ProjectMgmt.db")
cur = con.cursor()

cur.execute("""
    INSERT INTO user VALUES
        ('123', 'jordan', 'jordan@gmail.com', 'https://randomuser.me/api/portraits/men/2.jpg', '123')
""")

con.commit()
con.close()