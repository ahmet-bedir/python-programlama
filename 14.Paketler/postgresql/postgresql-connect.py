import psycopg2

dbConnect = psycopg2.connect(
    host="127.0.0.1",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432"
)

cur = dbConnect.cursor()
sql = """show data_directory;;"""
cur.execute(sql)

tableList = cur.fetchall()

for i in tableList:
    print(i)
    
dbConnect.close()