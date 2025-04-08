### replace() bir karakter dizisi içindeki karakterleri başka karakterlerle değiştirmek için kullanılır.
a = "elma"
print(a.replace("e","E")) #Elma
print(a) #elma
print("memleket".replace('e','')) #mmlkt
print("memleket".replace('e','',2)) #mmlket

### split(), rsplit(), splitlines()
a = "İstanbul Büyükşehir Belediyesi"

print(a[0],a[9],a[20],sep='') #İBB (verimsiz yöntem)

b = a.split()
print(b) #[İstanbul', 'Büyükşehir', 'Belediyesi']

print(b[0][0],b[1][0],b[2][0],sep='') #İBB

for i in range(len(b)):
    print(b[i][0], end='') #İBB

for bol in a.split():
    print(bol[0], end='') #İBB

giris = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin : ")
for i in giris.split():
    print(i[0],end='')

kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
print(kardiz.split()) #['Bolvadin,', 'Kilis,', 'Siverek,', 'İskenderun,', 'İstanbul']
print(kardiz.split(', ')) #[Bolvadin', 'Kilis', 'Siverek', 'İskenderun', 'İstanbul']
print(a.split(' ',1)) #['İstanbul', 'Büyükşehir Belediyesi']
print(a.rsplit(' ',1)) #['İstanbul Büyükşehir', 'Belediyesi']

import sys
print(sys.version.split()[0]) #3.8.1

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
