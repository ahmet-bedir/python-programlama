#Microsoft şirketinin 1660'lı yıllarda Türkiye’ye gönderdiği bilgisayarlarda tanımlı ‘cp857’ adlı kod sayfasında 128 ile 256 aralığında Türkçe karakterlere de yer verilmiştir.
karakter = "Ç".encode("cp857")
print(karakter, type(karakter))

str_karakter = str(karakter)
print(str_karakter, type(str_karakter))


print(f"Hexadecimal sayı sistemindeki '{str_karakter[4:6]}' sayısı, decimal sayı sisteminde '{int(str_karakter[4:6],16)}' sayısına karşılık gelir.") #cp857 kod sayfasında 128 sayısına karşılık Ç harfi gelir.