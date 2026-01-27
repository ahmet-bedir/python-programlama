import sqlite3

with sqlite3.connect('db.sqlite') as vt:
	im = vt.cursor()

	veriler = [('Fırat', 'Özgül', 'Adana'),
	('Ahmet', 'Söz', 'Bolvadin'),
	('Veli', 'Göz', 'İskenderun'),
	('Mehmet', 'Öz', 'Kilis')]

	# im.execute("""CREATE TABLE IF NOT EXISTS personel
	# (isim, soyisim, memleket)""")

	# for veri in veriler:
		# im.execute("""INSERT INTO personel VALUES
		# (?, ?, ?)""", veri)

	sql = "SELECT * FROM personel"
	im.execute(sql)
	veriler = im.fetchall()
	print(veriler)

	# vt.commit()

