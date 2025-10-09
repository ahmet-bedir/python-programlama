def kayit(isim="",soyisim="",sistem="",sehir="ankara"):
	print("-"*30)
	print("İsim :", isim)
	print("Soyisim :", soyisim)
	print("İşletim Sistemi :", sistem)
	print("Şehir :", sehir)
	print("-"*30)

kayit("ahmet","bedir","linux","kocaeli")
kayit("ali","koz","windows","kars")
kayit("unix","istanbul","ersin","şeker") #sıralama sırası değiiştimi sıkıntı oluyor.

kayit(sistem="dos",isim="can",soyisim="saka")


###
def sistem_blgisi():
	import sys
	print("\nSistemde kurulu Python'ın;")
	print("\tana sürüm numarası:", sys.version_info.major)
	print("\talt sürüm numarası:", sys.version_info.minor)
	print("\tminik sürüm numarası:", sys.version_info.micro)
	print("\nKullanılan işletim sisteminin;")
	print("\tadı:", sys.platform)

sistem_blgisi()

###
def uzunluk(kelime):
	i = 0
	for harf in kelime:
		i=i+1
	print(i)

uzunluk("python")
# diğer kodlar...
uzunluk("ali")
# diğer kodlar...
liste = ["bardak",'a',5,True]
uzunluk(liste)

