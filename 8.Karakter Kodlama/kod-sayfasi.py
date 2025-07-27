#Microsoft şirketinin 1660'lı yıllarda Türkiye’ye gönderdiği bilgisayarlarda tanımlı ‘cp857’ adlı kod sayfasında 128 ile 256 aralığında Türkçe karakterlere de yer verilmiştir.
karakter = "Ç".encode("cp857") #Burada kullandığımız encode() metodu herhangi bir karakteri herhangi bir karakter kodlama sistemine göre kodlayabiliriz. Mesela örnekte ‘Ç’ harfini ‘cp857’ adlı kod sayfasına göre kodladık ve bunların bu kod sayfasında hangi sayıya karşılık geldiğini bulduk.
print(karakter, type(karakter))

str_karakter = str(karakter)
print(str_karakter, type(str_karakter))


print(f"Hexadecimal sayı sistemindeki '{str_karakter[4:6]}' sayısı, decimal sayı sisteminde '{int(str_karakter[4:6],16)}' sayısına karşılık gelir. ('cp857' kod sayfasında 128 sayısına karşılık 'Ç' harfi gelir.)")

print(f"Hexadecimal sayı sistemindeki '{str("ü".encode("cp857"))[4:6]}' sayısı, decimal sayı sisteminde '{int(str("ü".encode("cp857"))[4:6],16)}' sayısına karşılık gelir. ('cp857' kod sayfasında 129 sayısına karşılık 'ü' harfi gelir.)")


#print("Ç".encode("ascii")) #ASCII kodlama sisteminde 'Ç' harfi bulunmadığı için hata alırız.
print("a".encode("ascii"))


print("Ç".encode("utf-8"))
print(int("c3",16))
print(int("87",16))