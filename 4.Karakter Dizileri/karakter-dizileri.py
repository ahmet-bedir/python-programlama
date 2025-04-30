### 
sayilar = "123456789"
for sayi in sayilar:
    print("{} x 2 = {}".format(sayi,int(sayi)*2))

### Karakter Dizilerinin Öğelerine Erişmek
print('#'*40)
a = "python"
print(a[0],a[
    1],a[2],a[3],a[4],a[5]) #p y t h o n
print(a[0]) #p
print(len(a)) #6
print(a[len(a)-1]) #n
print(a[-1]) #n
print(a[-5]) #y
print('#'*40)

for i in range(len(a)):
    print(a[i], end=' ') #p y t h o n
print("\n")
for i in range(5):
    print(a[i], end=' ') #p y t h o
print('\n','#'*40,sep='')

###
isim = input("İsminiz : ")
for i in range(len(isim)):
    print("isminizin {}.harfi : {}".format(i+1,isim[i]))

### Karakter Dizilerini Dilimlemek (karakter_dizisi[alınacak_ilk_öğenin_sırası:alınacak_son_öğenin_sırasının_bir_fazlası])
site = "www.google.com.tr"
print(site[0:3]) #www
print(site[4:10]) #google
print(site[15:18]) #tr

###
site1 = "www.google.com.tr"
site2 = "www.bing.com.tr"
site3 = "www.yahoo.com.tr"
for i in site1,site2,site3:
    print(i)
    print(i[4:-7])
    print(i[4:-4] + ".uk", "-"*25)
    
### bu atasözlerinin sonunda bulunan ünlem işaretlerini nokta işareti ile değiştirme.
ata1 = "Akıllı bizi arayıp sormaz deli bacadan akar!"
ata2 = "Ağa güçlü olunca  kul suçlu olur!"
ata3 = "Avcı ne kadar hile bilirse ayı da o kadar yol bilir!"
ata4 = "Lafla pilav pişse deniz kadar yağ benden!"
ata5 = "Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"
for ata in ata1, ata2, ata3, ata4, ata5:
    print('• ' + ata[0:-1] + '.')

###    
kardiz = "Sana Gül Bahçesi Vadetmedim"
print(kardiz[0:4]) #Sana
print(kardiz[:4]) #Sana
print(kardiz[17:27]) #Vadetmedim
print(kardiz[17:]) #Vadetmedim
print(kardiz[::-1]) #midemtedaV iseçhaB lüG anaS
print(kardiz[7:4:-1]) #lüG

print(reversed(kardiz))
#<reversed object at 0x00E8E250>
print(*reversed(kardiz), sep='')
#midemtedaV iseçhaB lüG anaS
for i in reversed(kardiz):
    print(i, sep="",end="")
    #midemtedaV iseçhaB lüG anaS
for i in range(len(kardiz)-1,-1,-1):
    print(kardiz[i], sep="",end="")
    #midemtedaV iseçhaB lüG anaS

### Karakter Dizilerini Alfabe Sırasına Göre Dizmek
a = "ahmet"
print(sorted(a)) #['a', 'e', 'h', 'm', 't']
print(type(sorted(a))) #<class 'list'>
print(*sorted(a)) #a e h m t
for i in sorted(a):
    print(i, end=" ") #a e h m t

### Türkçe karakterlerin düzgün sıralanması için...
import locale #locale modülü bize belli bir dilin kendine has özelliklerine göre programlama yapma imkanı verir. 
#locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254") #Windows için
locale.setlocale(locale.LC_ALL,"tr_TR") #GNU/Linux için
print(sorted("çicek",key=locale.strxfrm))

### Karakter Dizilerinde Değişiklik Yapma
# Python’da iki tür veri tipi bulunur: değiştirilemeyen veri tipleri (immutable datatypes) ve değiştirilebilen veri tipleri (mutable datatypes). Karakter dizileri değiştirilemeyen (immutable) bir veri tipidir.
a = "elma"; print(a, ':', id(a)) #elma : 140175547197360
a = 'E' + a[1:]; print(a, ':', id(a)) #Elma : 140005783201584

kardiz = "istihza"
kardiz = kardiz[:3] + "İH" + kardiz[5:]
print(kardiz) #istİHza



### dir() fonksiyonu python’daki bir nesnenin özellikleri hakkında bilgi verir. Mesela karakter dizilerinin bize hangi metotları sunduğunu görmek için kullanabiliriz.
print("str :", dir(str))

###
sayac = 0
for i in dir(""): #veya dir(str) veya dir("karakter")
    if "_" not in i[0]:
        sayac += 1
        print(sayac, '.', i, sep='')
print("Toplam :", sayac)

###
print(enumerate("istihza")) #<enumerate object at 0x00E3BC88>
print(*enumerate("istihza",1)) #(1, 'i') (2, 's') (3, 't') (4, 'i') (5, 'h') (6, 'z') (7, 'a')
for i in enumerate("istihza",1):
    print(i, end=' ') #(1, 'i') (2, 's') (3, 't') (4, 'i') (5, 'h') (6, 'z') (7, 'a')
for sira,metot in enumerate(dir(str),1):
    print("{}.{}".format(sira,metot))
    
###
tr_harfler = "şçöğüİı"
a = 0

while a < len(tr_harfler):
    print(tr_harfler[a], sep="\n")
    a += 1
###
tr_harfler = "şçöğüİı"

for tr_harf in tr_harfler:
    print(tr_harf)

###
import sys
print(sys.version[:6]) #3.12.1

print("{}.{}.{}".format(sys.version_info.major,sys.version_info.minor,sys.version_info.micro)) #3.12.1
# Python’ın 2.7 öncesi sürümleri için...
major = sys.version_info[0]
minor = sys.version_info[1]
micro = sys.version_info[2]
print(major, minor, micro, sep=".")