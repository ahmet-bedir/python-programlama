'''
range fonksiyonu.
range(ilk_sayı, son_sayı, atlama_degeri)
'''
for i in range(0, 11):
    print(i, end=' ') #0'dan 11'e kadar olan sayılar.(0 dahil, 11 hariç)
print('\n')
for i in range(11): #0'dan 11'e kadar
    print(i, end=' ')
print('\n')    
for i in range(3, 11): #3'den 11'e kadar
    print(i, end=' ')
print('\n')
for i in range(0, 11, 2): #0'dan 11'e kadar iki atlamalı
    print(i, end=' ')
print("\n")
for i in range(10, 0, -1): #sayıları tersten sıralar
    print(i, end=' ')
print('\n')

print(*range(10), sep=' ')


'''
pass deyimi ‘geçmek, pas geçmek’ gibi anlamda kullanılır.
'''

"""
while True:
    parola = input("Parola Belirleyin : ")
    if not parola:
        pass
    elif len(parola) in range(3, 9):
        print("Yeni Parolanız : ", parola)
        break
    else:
        print("Parola 8 Karakterden Uzun 3 Karakterden Kısa Olmamalı...")

#
while True:
    sayı = int(input("Bir Sayı Girin : "))
    if sayı == 0:
        break
    elif sayı < 0:
        pass
    else:
        print(sayı)

#
while True:
    s = input("Bir Sayı Girin : ")
    if s == "iptal":
        break
    if len(s) <= 3:
        continue
    print("En Fazla Üç Haneli Bir Sayı Girebilirsiniz.")
      

for i in range(3):
    print(i)
else:
    print("else")
    
for i in range(5):
    if i == 3:
        break
else:
    print("else")


karater_dizisi = "Merhebe dünye"
for harf in karater_dizisi:
    if harf == 'a':
        print("a harfi bulundu.")
        break
else:
    print("a harfi bulunamadı.")


###
sayilar = "1234567890"
sayi = "870"
for i in sayi:
    if i not in sayilar:
        print("Sayı Değerli Değil...")
        break
else:
    print("Sayı Değerli...")
        
"""