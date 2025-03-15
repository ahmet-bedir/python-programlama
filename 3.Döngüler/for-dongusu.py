print('-'*40)
tr_harfler = "çÇğĞıİöÖşŞüÜ"

print("for döngüsü ile türkçe harfler.")
for harf in tr_harfler:
    print(harf, end='  ')
print('\n','-'*40, sep='')

###
print("print fonksiyonu ile türkçe harfler.")
print(*tr_harfler, sep='  ')
print('-'*40)

###
print("while döngüsü ile türkçe harfler.")
a = 0
while a < len(tr_harfler):
    print(tr_harfler[a], end='  ')
    a += 1
print('\n','-'*40, sep='')

'''
sayilar = 123456789 #hata! çünkü sayılar üzerinde döngü kuramayız.
for sayi in sayilar:
    print(sayi)
'''
#Burada str_sayilar adlı değişkenin her bir öğesini bizim belirlediğimiz sayi adlı değişkenine aktardıkdan sonra, int() fonksiyonu yardımıyla bu öğeleri tek tek sayıya çevirdik ve her bir öğeyi 2 ile çarptık.
str_sayilar = "123456789"
for sayi in str_sayilar:
    print(int(sayi) * 2, end='  ')
print('\n', '-'*40, sep='')

#Burada int_sayilar adlı değişkeni önce stringe çevirip her bir öğesini bizim belirlediğimiz sayi adlı değişkenine aktardıkdan sonra, int() fonksiyonu yardımıyla bu öğeleri tek tek sayıya çevirdik ve her bir öğeyi 2 ile çarptık.
int_sayilar = 123456789
for sayi in str(int_sayilar):
    print(int(sayi) * 2, end='  ')
print('\n', '-'*40, sep='')
