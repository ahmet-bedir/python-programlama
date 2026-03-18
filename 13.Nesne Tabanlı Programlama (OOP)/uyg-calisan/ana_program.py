import calisan_modulu as cal
#from calisan_modulu import Calisan

print('='*45)
print("calisan_modulu.py dosyasının içeriği:", dir(cal), sep='\n')
print('='*45)
print("calisan_modulu.py dosyasındaki Calisan sınıfının içeriği:", dir(cal.Calisan), sep='\n')

print('='*45)
cal.Calisan.personel_sayisi()

p1 = cal.Calisan("ali")
p1.kabiliyet_ekle("bilişim")
p1.kabiliyet_ekle("iletişim")

p2 = cal.Calisan("erdi")
p2.kabiliyet_ekle("liderlik vasfı")
print('\n')

print('='*45)

cal.Calisan.personel_listesi()
cal.Calisan.personel_sayisi()
print('\n')

print('='*45)
p1.kabiliyet_listesi()
print('='*45)
p2.kabiliyet_listesi()