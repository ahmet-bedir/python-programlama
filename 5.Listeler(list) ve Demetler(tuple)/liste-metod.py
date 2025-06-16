###
liste_metod = [i for i in dir([]) if '_' not in i]
print(*liste_metod)

#append() metodunu, bir listeye öğe eklemek için kullanıyoruz.
liste = ["elma", "armut", "çilek"]
liste.append("erik") #append() metodu orijinal liste üzerinde doğrudan değişiklik yapmamıza izin veriyor.
print(liste)

#
liste = ["elma", "armut", "çilek"]
liste = liste + ["erik"] #artı işlecini kullandığımızda ise, orijinal listeyi değiştirmek yerine yeni bir liste oluşturuyoruz.
print(liste)

###
isletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
platformlar = ["IPhone", "Android", "S60"]
hepsi = isletim_sistemleri + platformlar
print(hepsi)

#
isletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
platformlar = ["IPhone", "Android", "S60"]

for platform in platformlar:
    isletim_sistemleri.append(platform)

print(isletim_sistemleri)

###
liste = [1, 2, 3]
#liste.append(1,2,3) #hata!
for i in [4, 5, 6]:
    liste.append(i)

print(liste)

#kullanıcının girdiği bütün sayıları birbiriyle çarpan bir uygulama.
toplam = 1
liste = []
while True:
    giris = input("Sayı (çıkış 'q') : ")
    if giris == 'q':
        break
    liste.append(giris)
    toplam *= int(giris)
    
if len(liste) < 2:
    print("En az iki sayı girilmeli!")
else:
    print("Toplam :", toplam)
