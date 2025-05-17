###
liste = ["Python", 1, 2.5, True]
print(f"Liste : {liste}, Türü : {type(liste)}")
for eleman in liste:
    print(f"Liste Elemanı : '{eleman}' Türü : {type(eleman)}")

# güncelleme
liste[-1] = "Php"
print(liste)
