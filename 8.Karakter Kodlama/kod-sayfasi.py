######################################
#print("Ç".encode("ascii")) #ASCII kodlama sisteminde 'Ç' harfi bulunmadığı için hata alırız.
print("a".encode("ascii")) #b'a'
print("a".encode("cp857")) #b'a'

print("a".encode("utf-8")) #b'a'
print("Ç".encode("utf-8")) #b'\xc3\x87'
print(int("c3",16)) #195
print(int("87",16)) #135

print("ß".encode("latin1"))
print(int("df",16)) #223