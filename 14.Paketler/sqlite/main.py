import sqlite3

vt = sqlite3.connect('db.sqlite')

im = vt.cursor()

# sql = "CREATE TABLE personel (isim, soyisim, memleket)" # yeni tablo oluşturma sorgusu

tbl_sql = "CREATE TABLE IF NOT EXISTS personel (id, isim, soyisim, memleket)" # koşullu tablo oluşturma sorgusu (aynı isimde tablo varsa hata vermez, yoksa yeni bir tablo oluşturur)

veri_sql = "INSERT INTO personel VALUES (1,'ali','tel','adana')" # tabloya veri girişi sorgusu

im.execute(tbl_sql)
im.execute(veri_sql)

vt.commit()
vt.close()
