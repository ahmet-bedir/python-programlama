import calisan as cal

p1 = cal.Calisan("ali")
p1.kabiliyet_ekle("üç harfli")
p1.kabiliyet_ekle("cin gibi")

p2 = cal.Calisan("erdi")
p2.kabiliyet_ekle("liderlik vasfı")
print('\n')

p1.personel_listesi()
print('\n')

p1.kabiliyet_listesi()
p2.kabiliyet_listesi()