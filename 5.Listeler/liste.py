### listelerde elemanlar değiştirilebilinir ve yeni eleman eklenebilir.
liste = ["Python", 1, 2.5, True]
print(f"Liste : {liste}, Türü : {type(liste)}")
for i, eleman in enumerate(liste,1):
    print(f"Listenin {i}. elemanı : '{eleman}' türü : {type(eleman)}")
print("Eleman Sayısı :", len(liste))

# listeyi güncelleme.
liste[1] = "Php"
print(liste)

# listeye eleman ekleme.
liste += [False, 'A', "Ali", 2]
print(liste)

# listeden eleman silme.
del liste[0]

# listede eleman arama.
eleman = "Python"
varMi = eleman in liste
if varMi:
    print(f"Liste içerisinde '{eleman}' elemanı bulunmaktadır.")
else:
    print(f"Liste içerisinde '{eleman}' elemanı bulunmamaktadır!")

##
