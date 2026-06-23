import psycopg2

db_connect = psycopg2.connect(
    host="127.0.0.1",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432"
)

cursor = db_connect.cursor()
sql = """
CREATE TABLE users (
    user_id INT AUTO_INCREMENT,
    user_name VARCHAR(30),
    PRIMARY KEY (user_id)
)"""
cur.execute(sql)

tableList = cur.fetchall()

for i in tableList:
    print(i)
    
dbConnect.close()