### capitalize() metodunun görevi karakter dizilerinin yalnızca ilk harfini büyütmektir.
print("python".capitalize()) #Python
a = "python programlama dili"
print(a.capitalize()) #Python programlama dili

for i in a.split():
    print(i.capitalize(), end=' ') #Python Programlama Dili

print("istanbul".capitalize()) #Istanbul

a = "istanbul"
if a.startswith("i"):
    a = "İ" + a[1:]
a = a.capitalize()
print(a) #İstanbul

### title() metodu birden fazla kelimeden oluşan karakter dizilerinin her kelimesinin ilk harflerini büyütür.
a = "python programlama dili"
print(a.title()) #Python Programlama Dili
print("izmit belediyesi".title()) #Izmit Belediyesi

metin = "istanbul büyükşehir belelediyesi"
if metin.startswith("i"):
    metin = "İ" + metin[1:]
metin = metin.title()
print(metin) #İstanbul Büyükşehir Belelediyesi

metin = "hükümet istifa! on iki ada"
for kelime in metin.split():
    if kelime.startswith('i'):
        kelime = 'İ' + kelime[1:]
    kelime = kelime.title()
    print(kelime, end=' ') #Hükümet İstifa! On İki Ada
    
### swapcase() metodu bir karakter dizisi içindeki büyük harfleri küçük harfe; küçük harfleri de büyük harfe dönüştürür.
kelime = "python"
print(kelime.swapcase()) #PYTHON
kelime = "PYTHON"
print(kelime.swapcase()) #python
kelime = "Python"
print(kelime.swapcase()) #pYTHON

kelime = "istanbul"
print(kelime.swapcase()) #ISTANBUL

for k in kelime:
    if k == 'i':
        kelime = kelime.replace('i','İ')
    elif k == 'İ':
        kelime = kelime.replace('İ','i')
    else:
        kelime = kelime.replace(k, k.swapcase())
print(kelime) #İSTANBUL

### casefold()
print("ß".lower()) #ß

print("ß".casefold()) #ss

### strip() metodu parametresiz olarak kullanıldığında, bir karakter dizisinin sağında veya solunda bulunan belli başlı karakterleri(boşluk, \n, \t vb) kırpar.
### lstrip() metodu karakter dizisinin sadece sol tarafındaki karakterleri kırpar.
### rstrip() metodu karakter dizisinin sadece sağ tarafındaki karakterleri kırpar.
kelime = " istihza "
print(kelime) #' istihza '

print(kelime.strip()) #'istihza'

print("kazak".strip('k').lstrip('a').rstrip('a')) #aza za z

metin = """
> Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından
> 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python
> olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.
> Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez.
> Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi
> grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır.
> Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
> bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır diyebiliriz.
"""
for i in metin.split():
    print(i.strip("> "), end=" ")

### join() metodu karakter dizisine ait bölünmüş parçaları tekrar bir araya getirir.
liste = ["Bjk","Jimnastik","Kulübü"]
print(' '.join(liste)) #Bjk Jimnastik Kulübü

### count() metodunun görevi bir karakter dizisi içinde belli bir karakterin kaç kez geçtiğini sorgulamaktır. 
sehir = "Kahramanmaraş"
print(sehir.count("a")) #5
print(sehir.count("a",6)) #3 (6. indisten sonra saymaya başlar)
print(sehir.count("a",6,9)) #1 (python’ın sorgulama işlemini hangi sıra aralıklarından gerçekleştireceğini gösterir)
parola = input("Parola Belirleyiniz : ")
kontrol = True
for i in parola:
    if parola.count(i) > 1:
        kontrol = False
if kontrol:
    print('Parolanız Onaylandı!')
else:
    print('Parolanızda Aynı Harfi Bir Kez Kullanabilirsiniz!')

#karakter dizisindeki bütün harflerin sayısını bulma.
metin = "python programlama dili"
tekle = ''
for harf in metin:
  if harf not in tekle and harf != ' ':
    tekle += harf
print("Metnin Orjinal Hali :", metin)
print("Metnin Tekrarlanmayan Harfleri :", tekle)
for harf in tekle:
    print("'{}' harfi '{}' metni içinde {} kez geçiyor...".format(harf,metin,metin.count(harf)))

### index() metodu karakterlerin, bir karakter dizisi içinde hangi sırada bulunduğunu öğrenmek için kullanılır.
### rindex() 
print("python".index('p')) #0
#print("python".index('z')) #hata!

kardiz = "adana"
print(kardiz.index("a", 0)) #0 (sıfırıncı indisten itibaren sorgulamaya başlar)
print(kardiz.index("a", 1)) #2
print(kardiz.index("a", 2)) #2
print(kardiz.index("a", 3)) #4
print(kardiz.index("a", 4)) #4

for i in range(len(kardiz)):
    print(kardiz.index("a", i)) #0 2 2 4 4

print(kardiz.index("a", 2, 3)) #2 (python’ın sorgulama işlemini hangi sıra aralıklarından gerçekleştireceğini gösterir)

kelime = "ada"
aranacak = 'd'
for i in range(len(kelime)-1):
    print(kelime.index(aranacak,i))
    

kelime = "ada"
aranacak = 'd'
for i in range(len(kelime)-1):
    print("i'nin değeri :", i)
    if i == kelime.index(aranacak, i):
        print("{}. sırada 1 adet {} harfi bulunuyor".format(i, aranacak))
    else:
        print("{}. sırada {} harfi bulunmuyor".format(i, aranacak))


print("python".index('p')) #0
print("python".rindex('n')) #5


##find, rfind()
kardiz = "adana"
print(kardiz.find("a")) #0
print(kardiz.rfind("a")) #4

print(kardiz.find("a",3)) #4
print(kardiz.find("c")) #-1

kardiz = "ada"
aranacak = 'b'
for i in range(len(kardiz)):
    print("i'nin değeri: ", i)
    if i == kardiz.find(aranacak, i):
        print("{}. sırada 1 adet {} harfi bulunuyor".format(i, aranacak))
    else:
        print("{}. sırada {} harfi bulunmuyor".format(i, aranacak))


##center()
print('|','a'.center(5),'|') #|  a  |

for i in range(10):
    print('|','*'.center(i),'|')
    
print('|',"python".center(8,'-'),'|', sep='') #|-python-|


##rjust(), ljust()
print('|','a'.ljust(5),'|', sep='') #|a    |
print('|','a'.rjust(5),'|', sep='')  #|    a|
print("ahmet".ljust(8,'.')) #ahmet...

for i in "elma","armut","muz","kayısı":
    print(i.ljust(8,'.'))


##zfill()
print('5'.zfill(2)) #05

for i in range(1,11):
    print(str(i).zfill(2), end=' ') #01 02 03 04 05 06 07 08 09 10
    
##partition(), rpartition()
print("istanbul".partition("an")) #('ist', 'an', 'bul')
print("istanbul".partition('f')) #('istanbul', '', '')
print("istizha".partition('i')) #('', 'i', 'stizha')
print("istizha".rpartition('i')) #('ist', 'i', 'zha')


##encode()
print("çilek".encode("cp1254")) #b'\xe7ilek'


##expandtabs()
a = "elma\tbir\tmeyvedir"
print(a) #elma	bir	meyvedir
print(a.expandtabs(10)) #elma      bir       meyvedir