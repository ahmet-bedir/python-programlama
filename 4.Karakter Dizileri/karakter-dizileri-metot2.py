### capitalize() metodunun görevi karakter dizilerinin yalnızca ilk harfini büyütmektir.
print("python".capitalize()) #Python
a = "python programlama dili"
print(a.capitalize()) #Python programlama dili

for i in a.split():
    print(i.capitalize(), end=' ') #Python Programlama Dili

##title()
print(a.title()) #Python Prog Dili

kardiz = "istanbul büyükşehir belelediyesi"
if kardiz.startswith("i"):
    kardiz = "İ" + kardiz[1:]
kardiz = kardiz.title()
#İstanbul Büyükşehir Belelediyesi
print(kardiz)

metin = "hükümet istifa on iki ada"
for kelime in metin.split():
    if kelime.startswith('i'):
        kelime = 'İ' + kelime[1:]
    kelime = kelime.title()
    print(kelime, end=' ')
    
##swapcase()
kardiz = "python"
print(kardiz.swapcase()) #PYTHON
kardiz = "PYTHON"
print(kardiz.swapcase()) #python
kardiz = "Python"
print(kardiz.swapcase()) #pYTHON

kardiz = "istanbul"
print(kardiz.swapcase()) #ISTANBUL
for k in kardiz:
    if k == 'i':
        kardiz = kardiz.replace('i','İ')
    elif k == 'İ':
        kardiz = kardiz.replace('İ','i')
    else:
        kardiz = kardiz.replace(k, k.swapcase())
print(kardiz) #İSTANBUL

##strip(), lstrip(), rstrip()
kardiz = " istihza "
print(kardiz) #' istihza '

print(kardiz.strip()) #'istihza'

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

##join()
list = ["Bjk","Jimnastik","Kulübü"]
print(' '.join(list)) #Bjk Jimnastik Kulübü

##count()
sehir = "Kahramanmaraş"
print(sehir.count("a")) #5


parola = input("Parola Belirleniz : ")
kontrol = True
for i in parola:
    if parola.count(i) > 1:
        kontrol = False
if kontrol:
    print('Parolanız Onaylandı!')
else:
    print('Parolanızda Aynı Harfi Bir Kez Kullanabilirsiniz!')


metin = "python programlama dili"
tekle = ''
for i in metin:
  if i not in tekle and i != ' ':
    tekle += i
print("Metnin Tekil Harfleri : ", tekle)
for i in tekle:
    print(i, " harfi '", metin, "' metni içinde ", metin.count(i), " kez geçiyor...", sep='')


##index(), rindex()
print("python".index('p')) #0

kardiz = "adana"
print(kardiz.index("a", 0)) #0
print(kardiz.index("a", 1)) #2
print(kardiz.index("a", 2)) #2
print(kardiz.index("a", 3)) #4
print(kardiz.index("a", 4)) #4


kelime = "adana"
aranacak = "d"
for i in range(len(kelime)):
    print(kelime.index(aranacak,i))

kardiz = "ada"
aranacak = 'd'
for i in range(len(kardiz)):
    print("i'nin değeri: ", i)
    if i == kardiz.index(aranacak, i):
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
