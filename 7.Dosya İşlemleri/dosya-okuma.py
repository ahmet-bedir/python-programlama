"""
    Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
    
    Kullanımı           : open(dosya_adi,dosya_erisme_modu)
    dosya_erisme_modu   : dosyayı hangi amaçla açtığımızı belirtir.
    "r" okuma modu      : okuma modu. belirtilen konumda dosya olmalıdır.
    seek                : cursor konumu

    Python’da bir dosyayı “r” kipinde açtığımızda o adda bir dosya olmalıdır, eğer o adda bir dosya yoksa hata alırız. Bir dosyayı okumak için read(), readline() ve readlines() adlı üç farklı metot kullanılır.
"""
###
f = open("log.txt","r")

r = f.read() #Dosyanın tüm içeriğini okur.

print("Tip:", type(r)) #Tip: <class 'str'>
print(r)

f.close()


###
f = open("./log.txt","r")

r = f.readline() #Dosyanın ilk satırını okur.

print("Tip:", type(r)) #Tip: <class 'str'>
print(r)

f.close()


###
f = open("log.txt") #Bir dosyayı okuma modunda açacaksanız "r" modunu belirtmeniz gerekmez.

r = f.readlines() #Dosyanın içedriği liste şeklinde okur.

print("Tip:", type(r)) #Tip: <class 'list'>
print(r) #['birinci satır\n', 'ikinci satır\n', 'üçüncü satır\n', 'dördüncü satır']

for satir in r:
    print(satir, end='')
    
f.close()


###
print(f.closed) #dosyanın kapatılma durumunu sorgular.


### dosyayı otomatik olarak kapatır.
with open("log.txt", encoding="utf-8") as file:
    print(file.read())

    file.seek(0)
    for i in file:
        print(i, end="")

print(file.closed)