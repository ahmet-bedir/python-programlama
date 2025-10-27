sozluk = {
	"kitap"       : "book",
	"bilgisayar"  : "computer",
	"programlama" : "programming"}

def ara(sozcuk):
	hata = "{} kelimesi sözlükte yok!"
	return sozluk.get(sozcuk, hata.format(sozcuk))

def ekle(kelime, ing_anlam):
	mesaj = "{} kelimesi sözlüğe eklendi!"
	sozluk[kelime] = ing_anlam
	print(mesaj.format(kelime))