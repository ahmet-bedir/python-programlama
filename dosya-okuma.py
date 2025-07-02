"""
#Python’da bir dosyayı “r” kipinde açtığımızda o adda bir dosya olmalıdır, eğer o adda bir dosya yoksa hata alırız. Bir dosyayı okumak için read(), readline() ve readlines() adlı üç farklı metot kullanılır.
f = open("/home/ahmet/Masaüstü/tahsilat.txt","r") #Eğer bir dosyayı okuma kipinde açacaksanız, bu “r” harﬁni hiç belirtmeseniz de olur.

r = f.read() #dosyanın tüm içeriğini okur.

print(type(r))
print(r)

f.close()
"""
###
f = open("/home/ahmet/Masaüstü/tahsilat.txt") 

r = f.readlines() #

print(type(r))

for satir in r:
    print(satir)

f.close()
