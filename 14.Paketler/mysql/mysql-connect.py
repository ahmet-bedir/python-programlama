import mysql.connector as my

baglanti = my.connect(
    host = "127.0.0.1", # 192.23.45.56
    user = "ahmet",
    password = "a",
    database = "db"
)
im = baglanti.cursor()

print(im)
