# Tek dosyayı kontrol işlemi.
dosya = open("1_os.jpg","rb")
veri = dosya.read(10)
print(veri)
print(veri[6:])
print(veri[6:11] in b"JFIF")

if veri[6:11] in [b"JFIF", b"Exif"]:
	print("JPEG Dosyasıdır.")
else:
	print("JPEG Dosyası Değildir!")

dosya.close()

# Çok dosyayı kontrol işlemi.
dosyalar = ["1","2","3"]
for dosya in dosyalar:
	with open(dosya,"rb") as dosya:
		print(dosya.read(10))