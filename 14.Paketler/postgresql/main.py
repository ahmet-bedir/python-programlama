import psycopg2

dbConnect = psycopg2.connect(
    host="127.0.0.1",
    database="postgres",
    user="postgres",
    password="p",
    port="5432"
)

cur = dbConnect.cursor()
sql = """SELECT * FROM kullanicilar;"""
cur.execute(sql)

tableList = cur.fetchall()

for i in tableList:
    print(i)
    
dbConnect.close()