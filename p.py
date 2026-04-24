import sqlite3

db_connect = sqlite3.connect("yeni.db")

cursor = db_connect.cursor()

# sql = """CREATE TABLE tablo1 (id, ad)"""
sql = """INSERT INTO tablo1 VALUES (1, 'ahmet')"""

cursor.execute(sql)
db_connect.commit()

db_connect.close()
