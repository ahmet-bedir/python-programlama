kelimeler = {
    "kitap"      : "book",
    "bilgisayar" : "computer",
    "programlama": "programming",
    "dil"        : "language",
    "defter"     : "notebook"
}

print(type(kelimeler))
print(len(kelimeler))

print('\n')
# Sözlük Öğelerine Erişme
print(kelimeler["kitap"])

for i in kelimeler:
    print(kelimeler[i])

print("\n")
#
sozluk = {
    "Ahmet Özkoparan": ["İstanbul", "Öğretmen", 34],
    "Mehmet Yağız"   : ["Adana", "Mühendis", 40],
    "Seda Bayrak"    : ["İskenderun", "Doktor", 30]
}
print(f"Memleket : {sozluk["Seda Bayrak"][0]}\nMeslek : {sozluk["Seda Bayrak"][1]}\nYaş : {sozluk["Seda Bayrak"][2]}")

print('\n')
#
kisiler = {
    "Ahmet Özkoparan": {
        "Memleket": "İstanbul",
        "Meslek"  : "Öğretmen",
        "Yaş"     : 34
    },
    "Mehmet Yağız"   : {
        "Memleket": "Adana",
        "Meslek"  : "Mühendis",
        "Yaş"     : 40
    },
    "Seda Bayrak"    : {
        "Memleket": "İskenderun",
        "Meslek"  : "Doktor",
        "Yaş"     : 30
    }
}
print(f"Memleket : {kisiler["Ahmet Özkoparan"]["Memleket"]}\nMeslek : {kisiler["Ahmet Özkoparan"]["Meslek"]}\nYaş : {kisiler["Ahmet Özkoparan"]["Yaş"]}")
