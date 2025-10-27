"""
# Modüller
import os

if os.name == 'posix':
	print('Hoşgeldin Linux Kullanıcısı!')
elif os.name == 'nt':
	print('Hoşgeldin Windows Kullanıcısı!')



print(os.getcwd()) # o anda hangi dizin altında bulunduğunuzu öğrenmek için.


print(os.makedirs('DATA')) # o anda içinde bulunduğunuz dizinde yeni bir dizin oluşturmak için.


### subprocess modülü, harici komutları Python içinden çalıştırabilmemizi sağlayan bir araçtır.
import subprocess as sp
sp.call(['bash','komut.sh'])


### webbrowser modülü, bilgisayarımızda kurulu internet tarayıcısını kullanarak internet sitelerini açabilmemizi sağlar.
import webbrowser as web
web.open('www.duckduckgo.com')


### import os gibi bir komutla bütün o isimleri içe aktarmak yerine, yalnızca kullanacağınız isimleri içe aktarmayı tercihde edebilirsiniz. Mesela os modülünün yalnızca name niteliğini kullanacaksanız:
from os import name, listdir
print(name)
#print(getcwd()) #hata!
print(listdir())
"""
# kendimizin oluşturduğu sozluk modüünü içe aktarıyoruz.
import sozluk 

print(dir(sozluk))

print(sozluk.sozluk)

bul = sozluk.ara("kitap")
print(bul)
bul = sozluk.ara("kalem")
print(bul)

sozluk.ekle("kedi","cat") #manuel ekleme.
while True:
	kelime = input("Yeni Kelime (Çıkış için `q` + Enter): ")
	if kelime == 'q':
		break
	ing_anlam = input("Kelimenin İngilizce Karşılığı: ")
	sozluk.ekle(kelime,ing_anlam) 
print(sozluk.sozluk)
	
sil = input("Silinecek Kelime: ")
sozluk.sil(sil)
	
print(sozluk.sozluk)
"""
import sys
print(sys.path) # Python bir modül dosyasını ararken, import komutunun verildiği dosyanın dizini ile birlikte, sys.path çıktısında görünen dizinlerin içine bakar.

sys.path.append('/home/ahmet/Masaüstü/') # path a yeni dizin ekliyoruz.
print(sys.path)
import prog
print(prog.a)
"""