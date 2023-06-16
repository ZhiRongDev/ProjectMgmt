import sqlite3

con = sqlite3.connect("../ProjectMgmt.db")
cur = con.cursor()

cur.execute("""
    INSERT INTO Task_list VALUES
        ('77889', 'project1', True ,'abc')
""")

con.commit()
con.close()