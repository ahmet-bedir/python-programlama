import sqlite3
# Eğer bu dizin içinde sqlite.db adlı bir veritabanı yoksa, bu ada sahip bir veritabanı oluşturulacaktır.
db_connect = sqlite3.connect('sqlite.db')
db_cursor = db_connect.cursor()

# yeni tablo oluşturma.
# sql = """CREATE TABLE personel (id, isim, soyisim, memleket);"""
# db_cursor.execute(sql)

# koşullu tablo oluşturma (aynı isimde tablo varsa hata vermez, yoksa yeni bir tablo oluşturur).
# sql = """CREATE TABLE IF NOT EXISTS personel (id, isim, soyisim, memleket);"""
# db_cursor.execute(sql)

# tabloya veri girişi.
sql = """INSERT INTO personel (isim, soyisim, memleket) VALUES ('ali','tel','adana');"""
db_cursor.execute(sql)
db_connect.commit()
print("Kayıt Eklendi...")

# tabloyu listeleme.
sql = """SELECT * FROM personel;"""
db_cursor.execute(sql)
table_list = db_cursor.fetchall()
print("Tablo Listesi:")
for i in table_list:
    print(i)

db_connect.close()
