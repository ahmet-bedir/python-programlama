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
# sorgu = re.search("güçlü",a)
#
# if sorgu != None:
#     print(f"'{sorgu.group()}' kelimesi karakter dizisinde geçmektedir.")
#     print("Konum:", sorgu.span())
# else:
#     print("Aranan kelime karakter dizisinde geçmemektedir!")

#
# liste = ["elma","armut","erik"]
# for i in liste:
#     sorgu = re.search("armut",i)
#     if sorgu:
#         print(f"'{sorgu.group()}' kelimesi liste içerisinde geçmektedir.")

