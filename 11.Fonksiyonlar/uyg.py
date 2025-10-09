def toplama(*sayilar):
	toplam = 0
	for sayi in sayilar:
		toplam += sayi
	print("Toplam :", toplam)

toplama(1,2,3,4,5)