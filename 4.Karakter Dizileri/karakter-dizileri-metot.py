### replace() bir karakter dizisi içindeki karakterleri başka karakterlerle değiştirmek için kullanılır.
kelime = "elma"
print(kelime.replace("e","E")) #Elma
print(kelime) #elma
print("memleket".replace('e','')) #mmlkt
print("memleket".replace('e','',2)) #mmlket

### split(), rsplit(), splitlines()
metin = "İstanbul Büyükşehir Belediyesi"

print(metin[0],metin[9],metin[20],sep='') #İBB (verimsiz yöntem)

kelimeler = metin.split()
print(kelimeler) #[İstanbul', 'Büyükşehir', 'Belediyesi']

print(kelimeler[0][0],kelimeler[1][0],kelimeler[2][0],sep='') #İBB (kendi tanımladığımız değişken dışında verimsiz yöntem)

for i in range(len(kelimeler)):
    print(kelimeler[i][0], end='') #İBB

for kelime in metin.split():
    print(kelime[0], end='') #İBB
    
##
giris = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin : ")
giris_kelimeler = giris.split()
for i in range(len(giris_kelimeler)):
    print(giris_kelimeler[i][0],end='')
##
giris = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin : ")
for kelime in giris.split():
    print(kelime[0],end='')

kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
print(kardiz.split()) #['Bolvadin,', 'Kilis,', 'Siverek,', 'İskenderun,', 'İstanbul']
print(kardiz.split(', ')) #[Bolvadin', 'Kilis', 'Siverek', 'İskenderun', 'İstanbul']
print(metin.split(' ',1)) #['İstanbul', 'Büyükşehir Belediyesi']
print(metin.rsplit(' ',1)) #['İstanbul Büyükşehir', 'Belediyesi']
##
import sys
print(sys.version.split()[0]) #3.12.1

##
metin = """Python programlama dili Guido
Van Rossum adlı Hollandalı bir programcı
tarafından 90'lı yılların başında
geliştirilmeye başlanmıştır.Çoğu insan,
isminin Python olmasına bakarak, bu
programlama dili, adını piton yılanından
aldığını düşünür.Ancak zannedildiğinin
aksine bu programlama dilinin adı piton
yılanından gelmez..."""
print(metin.splitlines())
print(metin.splitlines(True))

##lower()
print("Kocaeli".lower()) #kocaeli

isim = "Ali Er"
isim = isim.lower(); print(isim) #ali er
if isim == "ali er":
    print("İsim : Ali Er","Şehir : Kocaeli","Yaş : 43", sep="\n")
else:
    print("Aradığınız kişi veritabanında bulunmamaktadır!")

print("İstanbul Iğdır".replace('İ','i').replace('I','ı').lower()) #istanbul ığdır

##upper()
print("konya".upper()) #KONYA

print("izmit".upper()) #IZMIT
print("izmit".replace('i','İ').upper()) #İZMİT

##islower(), isupper()
print("python".islower()) #True
print("Python".islower()) #False
ad = "ali tonbul"
if not ad.islower():
    print("Sadece Küçük Harf Kullanın!")
else:
    print("İsminiz : ", ad)

print("PYTHON".isupper()) #True
print("Python".isupper()) #False

mesaj = """
SELAM
NABER
NASILSIN
Napıyosun
GEL"""
bol = mesaj.splitlines()
for i in bol:
    if i.isupper():
       print("Tamamı Büyük Harf Olmamalı!")
       break

##endswith()
print("izmit".endswith('it')) #True
d1 = "python.ogg"
d2 = "tkinter.mp3"
d3 = "pygtk.ogg"
d4 = "movie.avi"
d5 = "sarki.mp3"
d6 = "filanca.ogg"
d7 = "falanca.mp3"
d8 = "dosya.avi"
d9 = "perl.ogg"
d10 = "c.avi"
d11 = "c++.mp3"

for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
    if i.endswith(".mp3"):
        print(i)
    if i[-4:len(i)] == ".ogg":
        print(i)

##startswith()
for i in d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11:
    if i.startswith("p"):
        print(i)
