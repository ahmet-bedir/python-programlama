### % İşareti ile Biçimlendirme (Eski Yöntem)

parola = input("parola: ")

print("Girdiğiniz parola (%s) kurallara uygun bir paroladır!" %parola)

#
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

## veya
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

