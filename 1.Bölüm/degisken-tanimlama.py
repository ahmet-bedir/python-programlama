x, y, z = 1, "2", 3.0

print(x, type(x))
print(y, type(y))
print(z, type(z))

###################################################

import keyword
print("-" * 45)
print("Kullanabileceğimiz Fonksiyonlar (keyword) :\n", dir(keyword), sep="", end="\n\n")
a = keyword.kwlist
print("Tanımlayamayacağımız Değişken İsimleri :\n", a, sep="")
print("-" * 45)
print("Yasaklı Kelime Adedi :", len(a))
print("-" * 45, end="\n\n")

############################################

isletme = "Sefa Bilişim"
gun = 20
gidis_ucreti = 1.5
donus_ucreti = 1.4

masraf = gun * (gidis_ucreti + donus_ucreti)

print("-" * 31)
print("=== " + isletme + " ===")
print("-" * 31)
print("Çalışılan Gün Sayısı\t: ", gun)
print("İşe Gidiş Ücreti\t: ", gidis_ucreti)
print("İşten Dönüş Ücreti\t: ", donus_ucreti)
print("-" * 31)
print("Aylık Yol Masrafı\t: ", masraf)
print("-" * 31, end="\n\n")

############################################

cap = 16
yari_cap = cap / 2
pi = 3.14159

alan = pi * yari_cap * yari_cap
cevre = 2 * pi * yari_cap

print(45 * "-")
print("Yarıçapı " + str(int(yari_cap)) + " Olan Dairenin Alanı : " + str(alan))
print("Yarıçapı", int(yari_cap) ,"Olan Dairenin Çevresi :", cevre)
print(45 * "-", end="\n\n")

############################################

print(45 * "-")
print("İki üzeri üç :", 2**3) #8
print("Üç üzeri iki :", pow(3,2)) #9
print("Dörtün karekökü :", pow(4,0.5)) #2
print("Üç üzeri iki bölü iki kalan :", pow(3,2,2)) #1
print("Üç üzeri iki bölü üç kalan :", pow(3,2,3)) #0
print("-" * 45, end="\n\n")

############################################

ocak = mart = mayis = temmuz = agustos = ekim = aralik = 31
nisan = haziran = eylul = kasim = 30
subat = 28
mart_aylik_sarfiyat = 346
mart_fatura_tutari = 273.87

birim_fiyat = mart_fatura_tutari / mart_aylik_sarfiyat
gunluk_sarfiyat = mart_aylik_sarfiyat / mart
nisan_fatura = nisan * gunluk_sarfiyat * birim_fiyat
print("-" * 45)
print("Nisan Ayı Faturası : ", nisan_fatura)
print("-" * 45, end="\n\n")

############################################

print("-" * 45)
osman = "Araştırma Geliştirme Müdürü"
mehmet = "Proje Sorumlusu"

print("Osman :", osman)
print("Mehmet :", mehmet)
print("·—" * 22)
#Değisken değerlerini takas etme...
osman, mehmet = mehmet, osman
print("Osman :", osman)
print("Mehmet :", mehmet)
print("-" * 45)
