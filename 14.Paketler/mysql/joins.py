import mysql.connector

dbConnect = mysql.connector.connect(
    host="127.0.0.1",
    user="ahmet",
    password="a",
    database="marketdb"
)

dbCursor = dbConnect.cursor()
sql = """SELECT product_name, price, product_image, description, categoryid
FROM products;"""
dbCursor.execute(sql)
try:
    result = dbCursor.fetchall()    
    for product in result:
        print(product)
except mysql.connector.Error as err:
    print('hata:', err)
finally:
    dbConnect.close()
    print('database bağlantısı kapandı.')