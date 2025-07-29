######################################
for i in range(1, 5):
    print("{} bayt kullanırsak toplam 2**{:<2} = {:,} karakter kodlanabilinir.".format(i, i*8, (2**(i*8))))
    
    
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
for s in harfler:
    print("{:<5}{:<15}{} byte".format(s,str(s.encode("utf-8")), len(s.encode("utf-8"))))
    
#print("Ç".encode("ascii")) #ASCII kodlama sisteminde 'Ç' harfi bulunmadığı için hata alırız.
print("a".encode("ascii")) #b'a'
print("a".encode("cp857")) #b'a'
print("a".encode("utf-8")) #b'a'

print("Ç".encode("utf-8")) #b'\xc3\x87'(c387 sayısı utf-8 kod çözücüsünde 'Ç' harfine karşılık gelir)
sayi = (int("c387",16)) #50055
uzunluk = sayi.bit_length()
print(f"'Ç' harfi utf-8 kod çözücüsünde {uzunluk} bit, {uzunluk//8} bayt uzunluğundadır.")


"""
print("ß".encode("latin1")) #b'\xdf'
print(int("df",16)) #223

print("€".encode("cp1254")) #b'\x80'
print(int("80",16)) #128
"""