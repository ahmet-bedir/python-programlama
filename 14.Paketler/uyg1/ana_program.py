#yöntem 1 <kendi paketimizi içe aktarma>
import paket.islemler
import paket.metinler as m

print(dir(paket.islemler))
topla = paket.islemler.toplama(2,3)
print(topla)

print(dir(m))
m.metin1()