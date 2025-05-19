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

fstring = "f-string"
print(f"{{ {fstring} : f'{{ifade}}' şeklinde kullanılır. }}")

kaynak = "Python"
sene = 2022
print(f"{kaynak = } {sene = }")

print(f"|{kaynak:^20}|")
print(f"{kaynak:#^20}")
print(f"|{kaynak:<20}|")
print(f"|{kaynak:>20}|")
print(f"|{kaynak:<020}|")
