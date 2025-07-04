# Python’da bir dosyayı “w” kipinde açtığımızda, verdiğmiz adla bir dosya oluşturur, eğer o adda bir dosya ilgili dizin içinde zaten varsa, Python bu dosyayı sorgusuz sualsiz silip, yerine aynı adda başka bi dosya oluşturacaktır.
f = open("/home/ahmet/Masaüstü/tahsilat.txt","w")

f.write("Güven Yazılım : 150.500")

f.close()
