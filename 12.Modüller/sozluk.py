"""
belge dizisi (docstring) veya
belgelendirme dizisi (documentation string)
"""
sozluk = {
	"kitap"       : "book",
	"bilgisayar"  : "computer",
	"programlama" : "programming"}

def ara(kelime):
	hata = "{} kelimesi sözlükte yok!"
	return sozluk.get(kelime, hata.format(kelime))

def ekle(kelime, ing_anlam):
	mesaj = "{} kelimesi sözlüğe eklendi!"
	sozluk[kelime] = ing_anlam
	print(mesaj.format(kelime))

def sil(kelime):
	try:
		sozluk.pop(kelime)
	except KeyError as err:
		print(err, "kelimesi bulunamadı!")
	else:
		print("{} kelimesi sözlükten silindi!".format(kelime))