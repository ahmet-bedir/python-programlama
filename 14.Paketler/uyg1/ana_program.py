#yöntem 1 <kendi paketimizi içe aktarma>
import paket.islemler
import paket.metinler as m

#print(dir(paket.islemler))
topla = paket.islemler.toplama(2,3)
print("Toplama:", topla)

#print(dir(m))
m.metin1()

#yönem 2 <kendi paketimizi içe aktarma>
from paket import islemler
from paket import metinler as m

print("Çıkarma:", islemler.cikarma(2,1))

m.metin2()

#yönem 3 <modül içindeki nitelik ve metotlara öneksiz olarak erişmek için>
from paket.islemler import carpma

print("Çarpma:", carpma(2,3))

#yöntem 4 <bir paket içindeki bir modülün bütün nitelik ve metotlarını mevcut isim alanına olduğu gibi aktarmak için>>
from paket.islemler import *

print("Bölme :", bolme(8,2))