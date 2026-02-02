import sqlite3, os

dosya = 'db.sqlite'
dosya_mevcutmu = os.path.exists(dosya)

with sqlite3.connect('db.sqlite') as vt:
	im = vt.cursor()

	veriler = [('Fırat', 'Özgül', 'Adana'),
			   ('Ahmet', 'Söz', 'Bolvadin'),
			   ('Veli', 'Göz', 'İskenderun'),
			   ('Mehmet', 'Öz', 'Kilis')]

	im.execute("""CREATE TABLE IF NOT EXISTS personel
	(isim, soyisim, memleket)""")

	if not dosya_mevcutmu:
		for veri in veriler:
			im.execute("""INSERT INTO personel VALUES
			(?, ?, ?)""", veri)

			vt.commit()
