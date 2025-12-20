import re

print(dir(re))

# match() metodu bir karakter dizisinde yalnızca en başında belirtilen kelimenin geçip geçmediğini öğrenmek için kullanılır.

a = "python güçlü bir programlama dilidir."
sorgu = re.match("python",a)
print(sorgu)

sorgu = re.match("hon",a)
if sorgu == None:
    print("Aranan kelime karakter dizisini en başında geçmemektedir!")


sorgu = re.match("python",a)
print(sorgu)