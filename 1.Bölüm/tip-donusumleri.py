x = 2
y = 3.35
metin = "True"
mantiksal = False

print("Başlangıç Tip Değerleri")
print("x :", x, type(x))
print("y :", y, type(y))
print("metin :", metin, type(metin))
print("mantıksal :", mantiksal, type(mantiksal))

print("int => float")
x = float(x)
print("x :", x, type(x))

print("float => int")
y = int(y)
print("y :", y, type(y))

print("float int => str")
s = str(x) + str(y)
print("x + y :", s, type(s))

print("bool => int")
m = int(mantiksal)
print("mantıksal :", m, type(m))

print("str => bool")
s = bool(metin)
print("metin :", s, type(s))

###
metin = "6.5"
print(metin, type(metin)) #6.5 <class 'str'>

metin = float(metin)
print(metin, type(metin)) #6.5 <class 'float'>

metin = "6.5"
#metin = int(metin) #hata!
metin = int(float(metin))
print(metin, type(metin)) #6 <class 'int'>

metin = "6"
metin = int(metin)
print(metin, type(metin)) #6 <class 'int'>

metin = "6"
metin = float(metin)
print(metin, type(metin)) #6.0 <class 'float'>

### input fonksiyonundan gelen değer her zaman bi karakter dizisidir.
sayi1 = input("1.sayı: ")
sayi2 = input("2.sayı: ")
toplam = sayi1 + sayi2 #toplama işlemi yerine string birleştirme işlemi yapar.
print('Birleşim :', toplam)

#toplam = int(sayi1) + int(sayi2) #toplama işlemi yapar.
#print('Toplam :', toplam)

toplam = float(sayi1) + float(sayi2) #ondalıklı sayı girdiğimizde hata almamak için.
print('Toplam :', toplam)