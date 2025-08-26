# keys() metodu bir sözlüğün sadece anahtarlarını almak için kullanılır.
sozluk = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}
print(sozluk.keys())
print(list(sozluk.keys()))
print(tuple(sozluk.keys()))
print(''.join(sozluk.keys()))
print(str(sozluk.keys()))

# values() metodu bir sözlüğün sadece değerlerini almak için kullanılır.
print(sozluk.values())
print(list(sozluk.values()))
print(tuple(sozluk.values()))
#print(''.join(sozluk.values()))
print(str(sozluk.values()))
