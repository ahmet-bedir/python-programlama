import calisan_modulu as cal
from calisan_modulu import Calisan

print("calisan_modulu.py dosyasının içeriği:", dir(cal), sep='\n')
print("Calisan sınıfının içeriği:", dir(Calisan), sep='\n')

Calisan.personel_sayisi()

p1 = cal.Calisan("ali")
p1.kabiliyet_ekle("üç harfli")
p1.kabiliyet_ekle("cin gibi")

p2 = cal.Calisan("erdi")
p2.kabiliyet_ekle("liderlik vasfı")
print('\n')

Calisan.personel_listesi()
Calisan.personel_sayisi()
print('\n')

p1.kabiliyet_listesi()
p2.kabiliyet_listesi()