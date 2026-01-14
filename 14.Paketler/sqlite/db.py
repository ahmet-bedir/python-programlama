import sqlite3

vt = sqlite3.connect('yeni_vt.sqlite')

im = vt.cursor()

# im.execute("CREATE TABLE adres (isim, soyisim)")

im.execute("INSERT INTO adres (isim, soyisim) VALUES ('ahmet','bedir'),('ayşe','taner')")