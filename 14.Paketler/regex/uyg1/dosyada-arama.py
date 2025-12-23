### localda bulunan bi html dosyasında arama.
import re
from urllib.request import urlopen
f = urlopen("file:///home/ahmet/Masa%C3%BCst%C3%BC/python-programlama/14.Paketler/regex/uyg1/index.html")
# print(f.read())
for i in f:
    nesne = re.search(b'linux', i)
    if nesne:
        print(nesne.group())

###
ara = input("Aranacak kelime: ")
f = urlopen("file:///home/ahmet/Masa%C3%BCst%C3%BC/python-programlama/14.Paketler/regex/uyg1/index.html")
veri = str(f.read())
print(veri,type(veri))
nesne = re.search(ara, veri)

if nesne:
    print("kelime bulundu:", nesne.group())
else:
    print("kelime bulunamadı!:", ara)

"""
import re
from urllib.request import urlopen
kelime = input("python-istihza.yazbel.com'da aramak istediğiniz kelime: ")
f = urlopen("https://python-istihza.yazbel.com/")
data = str(f.read())
nesne = re.search(kelime, data)

if nesne:
print("kelime bulundu:", nesne.group())
else:
print("kelime bulunamadı!:", kelime)
"""