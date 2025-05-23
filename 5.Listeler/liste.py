### listelerde elemanlar değiştirilebilinir ve yeni eleman eklenebilir.
liste = ["Python", 1, 2.5, True]
print(f"Liste : {liste}, Türü : {type(liste)}")

print(liste[0])
print(liste[1])
print(liste[2])
print(liste[3])
#print(liste[4]) #hata! liste 4 elemanlı bir liste, biz olmayan elemanı yazdıramayız.

for i, eleman in enumerate(liste,1):
    print(f"Listenin {i}. elemanı : '{eleman}' türü : {type(eleman)}")
print("Eleman Sayısı :", len(liste))

# listeyi güncelleme.
liste[1] = "Php"
print("Listenin 2.elemanı 'Php' ile değiştirildi.")
print(liste)

# listeye eleman ekleme.
liste += [False, 'A', "Ali", 2]
print("Listeye 4 eleman daha eklendi.")
print(liste)

# listeden eleman silme.
del liste[0]
print("Listenin ilk elemanı silindi.")
print(liste)

# listede eleman arama.
eleman = "Python"
varMi = eleman in liste
if varMi:
    print(f"Liste içerisinde '{eleman}' elemanı bulunmaktadır.")
else:
    print(f"Liste içerisinde '{eleman}' elemanı bulunmamaktadır!")


