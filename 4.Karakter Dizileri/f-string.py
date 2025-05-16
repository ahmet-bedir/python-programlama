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