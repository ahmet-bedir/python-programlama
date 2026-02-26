import mysql.connector as mysql

baglanti = mysql.connect(
    host = "127.0.0.1", # 192.23.45.56
    user = "ahmet",
    password = "a",
    database = "db"
)

imlec = baglanti.cursor()
sql = """SELECT * FROM urunler;"""
imlec.execute(sql)
print(imlec.fetchall())
imlec.close()
