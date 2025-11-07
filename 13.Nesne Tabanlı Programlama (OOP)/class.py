sesli_harfler = 'aeıioöuü'
sayac = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler
    
for harf in kelime:
    if seslidir(harf):
        sayac += 1

mesaj = "'{}' kelimesinde {} tane sesli harf vardır!"
print(mesaj.format(kelime, sayac))