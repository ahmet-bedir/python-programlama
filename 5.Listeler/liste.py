### listeler değiştirilen (mutable) veri tipleridir.
# liste = ["Python", 1, 2.5, [True,False]]
# print(f"Liste : {liste}, Türü : {type(liste)}")
#
# print(liste[0])
# print(liste[1])
# print(liste[2])
# print(liste[3][0])
# print(liste[3][1])
# print(liste[-1])
# print(liste[0:2])
# print(liste[::-1])
# print(liste[4]) #hata! liste 4 elemanlı bir liste, biz olmayan elemanı yazdıramayız.

# yeni_liste = liste[3]
# print(yeni_liste[0])
# print(yeni_liste[1])

# for i in range(len(liste)):
#     print("{} -> {}".format(i+1,liste[i]))
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
liste = list(range(200))
print(liste)


### listeyi güncelleme.
liste = ["Python", 1, 2.5, [True,False]]
liste[1] = "Php"
print("Listenin 2.elemanı 'Php' ile değiştirildi.")
print(liste)

###
liste = [1, 2, 3]
print(liste)
liste[0:len(liste)] = 5, 6, 7 #liste[:] = 5, 6, 7
print(liste)

### listeye eleman ekleme.
liste += [False, 'A', "Ali", 2]
print("Listeye 4 eleman daha eklendi.")
print(liste)

### listeleri birleştirme.
derlenen_diller = ["C", "C++", "C#", "Java"]
yorumlanan_diller = ["Python", "Perl", "Ruby"]
programlama_dilleri = derlenen_diller + yorumlanan_diller
print(programlama_dilleri)

#Kullanıcı tarafından girilen beş adet sayının ortalamasını hesaplayan program.
sayilar = 0
for i in range(5):
    sayilar += int(input("Sayı : "))

print("Ortalama : ", sayilar/5)

#Kullanıcı tarafından girilen beş adet sayıyı listeye ekleyip ortalamasını hesaplayan program.
sayilar = []
toplam = 0
for i in range(5):
    print(f"{i+1}.", end='')
    sayi = int(input("Sayı : "))
    sayilar += [sayi]
print('#'*25)  
for i in range(5):
    print(f"{i+1}.sayı : {sayilar[i]}")
    toplam += sayilar[i]

print("Ortalama :", toplam/5)

#Kullanıcı tarafından sınırsız girilen sayıların ortalamasını hesaplayan program.
sayilar = list()
toplam = 0
while True:
    sayi = input("Sayı (çıkış 'q') : ")
    if sayi == "q":
        break
    sayilar += [sayi]
print('#'*25)
for i,sayi in enumerate(sayilar,1):
    toplam += int(sayi)
    print(f"{i}.sayı : {sayi}")

print("Ortalama :", toplam/len(sayilar))



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