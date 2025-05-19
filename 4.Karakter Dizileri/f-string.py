###
isim = 'Buğra'
print(f'Selam {isim}!')

##
isim = 'Ahmet'
yas = 36
metin = f'Benim adım {isim} ve ben {yas} yaşındayım.'
print(metin)

## aynı işlem format() metoduyla...
isim = 'Ahmet'
yas = 36
metin = 'Benim adım {} ve ben {} yaşındayım.'
print(metin.format(isim,yas))

#
sayi1 = 3
sayi2 = 2
print(F'{sayi1} + {sayi2} = {sayi1+sayi2}')

#
print(f'Sayıların toplamı {int(input("Birinci sayıyı girin: ")) + int(input("İkinci sayıyı girin: "))} eder.')


fstring = "f-string"
f"{{ {fstring}: f'{{ifade}}' şeklinde kullanılır. }}"
"{ f-string: f'{ifade}' şeklinde kullanılır. }"

kaynak = "Python İstihza"
yıl = "2022"
f"{kaynak=} {yıl=}"
kaynak='Python İstihza' yıl='2022'

istihza = "Python Istihza"
print(f"|{istihza:^30}|")

print(istihza.center(30))