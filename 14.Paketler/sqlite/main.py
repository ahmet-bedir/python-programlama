import sqlite3

vt = sqlite3.connect('vt.sql')

im = vt.cursor()

# sql = "CREATE TABLE personel (isim, soyisim, memleket)" # yeni tablo oluşturma sorgusu
sql = """CREATE TABLE IF NOT EXISTS personel
(isim, soyisim, memleket)""" # koşullu tablo oluşturma sorgusu (aynı isimde tablo varsa hata vermez, yoksa yeni bir tablo oluşturur)

im.execute(sql)