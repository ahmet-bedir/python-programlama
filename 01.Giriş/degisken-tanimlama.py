### Çoklu Atama - Tek satırda birden fazla değişken atama.

x, y, z = 1, "2", 3.0

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Aynı Değeri Birden Fazla Değişkene Atama
x = y = z = 4 # x, y, z = 4, 4, 4
print(x, y, z)

#################################################

import keyword
print("Kullanabileceğimiz Fonksiyonlar (keyword) :\n", dir(keyword), sep="", end="\n\n")

a = keyword.kwlist
print("Tanımlayamayacağımız Değişken İsimleri :\n", a, sep="")
print("-" * 45)
print("Yasaklı Kelime Adedi :", len(a))

###
import keyword

liste = keyword.kwlist
for i,eleman in enumerate(liste,1):
    print(f"{i}:{eleman}")

#################################################

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

################################################

cap = 16
yari_cap = cap / 2
pi = 3.14159

alan = pi * yari_cap * yari_cap
cevre = 2 * pi * yari_cap

print("Yarıçapı " + str(int(yari_cap)) + " Olan Dairenin Alanı : " + str(alan))
print("Yarıçapı", int(yari_cap) ,"Olan Dairenin Çevresi :", cevre)

################################################

ocak = mart = mayis = temmuz = agustos = ekim = aralik = 31
nisan = haziran = eylul = kasim = 30
subat = 28
mart_aylik_sarfiyat = 346
mart_fatura_tutari = 273.87

birim_fiyat = mart_fatura_tutari / mart_aylik_sarfiyat
gunluk_sarfiyat = mart_aylik_sarfiyat / mart
nisan_fatura = nisan * gunluk_sarfiyat * birim_fiyat

print("Nisan Ayı Faturası : ", nisan_fatura)

################################################

osman = "Araştırma Geliştirme Müdürü"
mehmet = "Proje Sorumlusu"

print("Osman :", osman)
print("Mehmet :", mehmet)

#Değisken değerlerini takas etme...
osman, mehmet = mehmet, osman
print("Osman :", osman)
print("Mehmet :", mehmet)

#################################################

# Bir listeden değişkenlere atama
koordinatlar = [41.01, 28.97]
print(koordinatlar, type(koordinatlar))  # [41.01, 28.97] <class 'list'>

enlem, boylam = koordinatlar
print(f"Enlem: {enlem} {type(enlem)}, Boylam: {boylam} {type(boylam)}")  # Enlem: 41.01 <class 'float'>, Boylam: 28.97 <class 'float'>

# Karakter dizisinden değişkenlere atama
koordinatlar = "41.01, 28.97"
print(koordinatlar, type(koordinatlar))  # 41.01, 28.97 <class 'str'>

enlem, boylam = koordinatlar.split(", ")
enlem = float(enlem)
boylam = float(boylam)
print(f"Enlem: {enlem} {type(enlem)}, Boylam: {boylam} {type(boylam)}")  # Enlem: 41.01 <class 'float'>, Boylam: 28.97 <class 'float'>

# Fonksiyon dönüş değerleriyle
def bolme_islemi(a, b):
    bolum = a // b
    kalan = a % b
    return bolum, kalan

sonuc, kalan = bolme_islemi(17, 5)
print(sonuc, type(sonuc))  # 3 <class 'int'>
print(kalan, type(kalan))  # 2 <class 'int'>
print(f"17 / 5 = {sonuc}, kalan {kalan}")  # 17 / 5 = 3, kalan 2

##################################################
