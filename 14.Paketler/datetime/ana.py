import datetime

simdiki_tarih = datetime.datetime.now()

print(simdiki_tarih)
print(f"{simdiki_tarih.day}/{simdiki_tarih.month}/{simdiki_tarih.year}")

bugun = datetime.datetime.today()

print(bugun)

print(datetime.datetime.ctime(simdiki_tarih))