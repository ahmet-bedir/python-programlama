# Rastgele 6 adet sayı üretme.
def sayi_uret(basla=0,bitis=10,adet=5):
	import random
	sayilar = set()

	while len(sayilar) < adet:
		sayilar.add(random.randint(basla,bitis))
		#print(sayilar)
	return sayilar


a = sayi_uret(0,5,5)
print(a)