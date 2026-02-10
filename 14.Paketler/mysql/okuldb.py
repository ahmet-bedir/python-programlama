from mysql.connector import connect

with connect(host='localhost', user = "ahmet", password = "a", database = "db") as vt:
    imlec = vt.cursor()
    # imlec.execute("CREATE DATABASE okuldb;")
    imlec.execute("SELECT * FROM urunler;")
    print(imlec.fetchall())
