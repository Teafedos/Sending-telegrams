import sqlite3

con = sqlite3.connect('base.db')
cur = con.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS users(
user TEXT)
""")
con.commit()
con.close()
