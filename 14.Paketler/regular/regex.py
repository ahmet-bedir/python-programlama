import re

# print(dir(re))

# match() metodu bir karakter dizisinde yalnızca en başında belirtilen kelimenin geçip geçmediğini öğrenmek için kullanılır.

a = "python güçlü bir programlama dilidir."

# sorgu = re.match( "python",a)
# if sorgu:
#     print(f"'{sorgu.group()}' kelimesi karakter dizisinin en başında geçmektedir.")
#     print("Konum:", sorgu.span())
# else:
#     print("Aranan kelime karakter dizisinin en başında geçmemektedir!")
#
# # alternatif
# bol = a.split()
# print(bol[0] == "python")
# print(a.startswith("python"))

# search() metodu karakter dizisinin genelinde belirtilen kelimenin geçip geçmediğini öğrenmek için kullanılır.
sorgu = re.search("güçhhlü",a)

print(sorgu.group())