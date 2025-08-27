# keys() metodu bir sözlüğün sadece anahtarlarını almak için kullanılır.
sozluk = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}
print(sozluk.keys())
print(list(sozluk.keys()))
print(tuple(sozluk.keys()))
print(''.join(sozluk.keys()))
print(str(sozluk.keys()), end='\n\n')

# values() metodu bir sözlüğün sadece değerlerini almak için kullanılır.
print(sozluk.values())
print(list(sozluk.values()))
print(tuple(sozluk.values()))
print(''.join([str(i) for i in sozluk.values()]))
print(str(sozluk.values()), end='\n\n')

# items() metodu, bir sözlüğün hem anahtarlarını hem de değerlerini aynı anda almamızı sağlar:
print(sozluk.items())

#
for anahtar, deger in sozluk.items():
    print("{} = {}".format(anahtar, deger))

# get() metodu sözlükte kelime sorgulama için kullanılır.
ing_sozluk = {
    "dil"       : "language",
    "bilgisayar": "computer",
    "masa"      : "table"}

sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız : ")

print(ing_sozluk.get(sorgu, "Bu kelime veritabanımızda yoktur!"))