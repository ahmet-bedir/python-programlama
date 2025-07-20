with open("1_os.jpg","rb") as dosya:
	data = dosya.read(10)
	print(data)
	print(data[:4] in b"JFIF")