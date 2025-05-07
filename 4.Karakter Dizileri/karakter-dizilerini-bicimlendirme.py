### % İşareti ile Biçimlendirme (Eski Yöntem)

parola = input("parola: ")

print("Girdiğiniz parola (%s) kurallara uygun bir paroladır!" %parola)

# s harfi karakter dizilerini ve karakter dizisine çevrilebilen değerleri temsil eder.
print("%s ve %s iyi bir ikilidir!" %("Python","Django"))

# hata! çünkü karakter dizisi içindeki %s işaretlerinin sayısı ile karakter dizisi dışında bu işaretlere karşılık gelen değerlerin sayısı birbirini tutmuyor.
print("Benim adım %s , soyadım %s " %"Ali")

#
kelime = "istihza"
for sira, karakter in enumerate(kelime, 1):
    print("%s.karakter '%s'" %(sira, karakter))

#
for i in range(1,11):
    print("%%%s" %i)

# % ile s işaretleri arasına yerleştirdiğimiz sayı, biçimlendirilecek karakter dizisinin toplam kaç karakterlik yer kaplayacağını gösteriyor.
for i in dir(str):
    print("%15s" %i)

for i in dir(str):
    print("|%15s|" %i)
for i in dir(str):
    print("|%-15s|" %i)

##
dil = "Python Programlama Dili"
sayfa = """
<html>
    <head>
        <title> %s </title>
    </head>
    <body>
        <h1> %s </h1>
        <p> Web sitemize hoşgeldiniz! Konumuz: %s </p>
    </body>
</html>
"""
print(sayfa %(dil,dil,dil))

## veya tekrardan kaçınmak için:
dil = "Python Programlama Dili"
sayfa = """
<html>
    <head>
        <title> %(d)s </title>
    </head>
    <body>
        <h1> %(d)s </h1>
        <p> Web sitemize hoşgeldiniz! Konumuz: %(d)s </p>
    </body>
</html>
"""
print(sayfa %{"d":dil})

# "%(değişken_adı)s " % {"değişken_adı": "değişken_değeri"}
print("Depoda %(miktar)s kilo %(ürün)s kaldı" %{"ürün": "elma", "miktar": 25})

### d harﬁ sayıları temsil eder.
print("Şubat ayı bu yıl %d gün çekiyor" %28)

#
print("Şubat ayı bu yıl %d gün çekiyor" %"28") #hata! Çünkü d harﬁ yalnızca sayı değerleri temsil edebilir, bu harﬂe birlikte karakter dizilerini kullanamayız.

print("%d" %10.3) #10

#
sayi = input("Sayı: ")

print("%d" %float(sayi))

### o harf octal (sekizli) kelimesinin kısaltmasıdır. Adından da anlaşılacağı gibi, sekizli düzendeki sayıları temsil eder. Dolayısıyla bu harﬁ kullanarak onlu düzendeki bir sayıyı sekizli düzendeki karşılığına dönüştürebilirsiniz.

#
print("{} ve {} iyi bir ikilidir!".format("Django", "Python"))

