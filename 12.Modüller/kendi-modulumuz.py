# Bulunduğumuz dizinde bulunan kendimizin oluşturduğu "sozluk" modülünü içe aktarıyoruz.
import sozluk 

print(dir(sozluk))

print(sozluk.sozluk)

bul = sozluk.ara("kitap")
print(bul)
bul = sozluk.ara("kalem")
print(bul)

###
sozluk.ekle("kedi","cat") #manuel ekleme.
while True:
	kelime = input("Yeni Kelime (Çıkış için `q` + Enter): ")
	if kelime == 'q':
		break
	ing_anlam = input("Kelimenin İngilizce Karşılığı: ")
	sozluk.ekle(kelime,ing_anlam) 
	
print(sozluk.sozluk)

###
sil = input("Silinecek Kelime: ")
sozluk.sil(sil)
	
print(sozluk.sozluk)
