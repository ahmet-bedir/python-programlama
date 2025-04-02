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
    
kardiz = "Sana Gül Bahçesi Vadetmedim"
#print(kardiz[0:4]) #Sana
#print(kardiz[:4]) #Sana
#print(kardiz[17:27]) #Vadetmedim
#print(kardiz[17:]) #Vadetmedim
#print(kardiz[::-1]) #midemtedaV iseçhaB lüG anaS
#print(kardiz[7:4:-1]) #lüG

#reversed(kardiz)
#<reversed object at 0x00E8E250>
#print(*reversed(kardiz), sep='')
#midemtedaV iseçhaB lüG anaS
#for i in reversed(kardiz):
    #print(i, sep="",end="")
    #midemtedaV iseçhaB lüG anaS

###Karakter Dizilerini Alfabe Sırasına Göre Dizmek
#print(sorted("ahmet")) #['a', 'e', 'h', 'm', 't']
#print(*sorted("ahmet")) #a e h m t
#for i in sorted("ahmet"):
    #print(i, end=" ") #a e h m t

#import locale
#locale.setlocale(locale.LC_ALL,"tr_TR")
#print(sorted("çicek",key=locale.strxfrm))

###Karakter Dizilerinde Değişiklik Yapma
#a = "elma"; print(a, ':', id(a)) #elma : 140175547197360
#a = 'E' + a[1:]; print(a, ':', id(a)) #Elma : 140005783201584

#kardiz = "istihza"
#kardiz = kardiz[:3] + "İH" + kardiz[5:]
#print(kardiz) #istİHza

###
"""
sesli_harfler = "aAeEıIiİoOöÖuUüÜ "
sessiz_harfler = "bBcCçÇdDfFgGğĞhHjJkKlLmMnNpPrRsSşŞtTvVyYzZ "
sesli = ""
sessiz = ""

kelime = "AhmeT"
for i in kelime: #kelime değişkenindeki her karakteri 'i' değişkenine attık
    if i in sesli_harfler: #'i' sesli_harfler değişkeninin içerisinde varsa...
        sesli += i #'sesli' ye ekle
    else:
        sessiz += i #yoksa 'sessiz' e ekle
print("Kelime : ", kelime)
print("Sesliler : ", sesli)
print("Sessizler : ", sessiz)
"""

#print("str : ", dir(str))
#print("int : ", dir(int))
#print("float : ", dir(float))
#print('complex : ', dir(complex))

sayac = 0
#for i in dir(""):
    #if "_" not in i[0]:
        #sayac += 1
        #print(sayac, '.', i, sep='')
#print("Toplam : ", sayac)

#print(enumerate("istihza")) #<enumerate object at 0x00E3BC88>
#print(*enumerate("istihza",1)) #(1, 'i') (2, 's') (3, 't') (4, 'i') (5, 'h') (6, 'z') (7, 'a')
#for i in enumerate("istihza"):
    #print(i, end=' ') #(0, 'i') (1, 's') (2, 't') (3, 'i') (4, 'h') (5, 'z') (6, 'a') 
#for sira,metot in enumerate(dir(str)):
    #if not '_' in metot[0]:
        #print(sira, '.', metot)
        #pass
    
import sys
#print(sys.version[:5]) #3.8.1

#print("{}.{}.{}".format(sys.version_info.major,sys.version_info.minor,sys.version_info.micro)) #3.8.1

major = sys.version_info[0]
minor = sys.version_info[1]
micro = sys.version_info[2]
#print(major, minor, micro, sep=".") #3.8.1



