### listelerde elemanlar değiştirilebilinir ve yeni eleman eklenebilir.
liste = ["Python", 1, 2.5, [True,False]]
# print(f"Liste : {liste}, Türü : {type(liste)}")
#
# print(liste[0])
# print(liste[1])
# print(liste[2])
# print(liste[3][0])
# print(liste[3][1])
# print(liste[4]) #hata! liste 4 elemanlı bir liste, biz olmayan elemanı yazdıramayız.
#
for i in range(len(liste)):
    print("{} -> {}".format(i+1,liste[i]))
# for i, eleman in enumerate(liste,1):
#     print(f"Listenin {i}. elemanı : '{eleman}' türü : {type(eleman)}")
#
# print("Eleman Sayısı :", len(liste))
# print("Kullanabileceğimiz metodlar :\n", dir(list), "\n", type(dir([])), sep='')
#
# bldy = "İzmit Büyükşehir Belediyesi"
# print(bldy, type(bldy))
# s_bldy = bldy.split()
# print(s_bldy, type(s_bldy))
#
##
# sayilar = [[0, 10], [6, 60], [12, 54], [67, 99]]
# for i in sayilar:
#     print(*range(i[0],i[1])) #print(*range(*i))
#
## list fonksiyonu.
# alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
# liste = list(alfabe)
# print(liste)
#
## sıfırdan ikiyüze kadar olan sayılardan bir liste oluşturma.
# liste = list(range(200))
# print(liste)
#
#
#
#
# listeyi güncelleme.
# liste[1] = "Php"
# print("Listenin 2.elemanı 'Php' ile değiştirildi.")
# print(liste)
#
# listeye eleman ekleme.
# liste += [False, 'A', "Ali", 2]
# print("Listeye 4 eleman daha eklendi.")
# print(liste)
#
# listeden eleman silme.
# del liste[0]
# print("Listenin ilk elemanı silindi.")
# print(liste)
#
# listede eleman arama.
# eleman = "Python"
# varMi = eleman in liste
# if varMi:
#     print(f"Liste içerisinde '{eleman}' elemanı bulunmaktadır.")
# else:
#     print(f"Liste içerisinde '{eleman}' elemanı bulunmamaktadır!")
#
#
#