dosya = open("1_os.jpg","rb")
veri = dosya.read(10)
print(veri)
print(veri[6:])

print(veri[6:11] in b"JFIF")
dosya.close()