"""
    Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
    
    Kullanımı           : open(dosya_adi,dosya_erişme_modu)
    dosya_erişme_modu   : dosyayı hangi amaçla açtığımızı belirtir.
    "r" okuma modu      : okuma modu. belirtilen konumda dosya olmalıdır.
    seek                : cursor konumu
"""

f = open("log.txt",encoding="utf-8")

print("dosyanın tamamını okunur :\n", f.read(), sep='')

f.seek(0) #cursör en başa gelir.


print("dosyanın ilk satrı okunur :\n", f.readline(), sep='')

f.seek(0)
print("dosyanın satırları liste şeklinde okunur :\n", f.readlines(), sep='')

f.seek(0)
for satir in f.readlines():
    print(satir, end='')

f.close()

print(f.closed) #dosyanın kapatılma durumunu sorgular.


### dosyayı otomatik olarak kapatır.
with open("log.txt", encoding="utf-8") as file:
    print(file.read())

    file.seek(0)
    for i in file:
        print(i, end="")

print(file.closed)