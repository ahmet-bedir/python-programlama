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

#
print(f'Sayıların toplamı {int(input("Birinci sayıyı girin: ")) + int(input("İkinci sayıyı girin: "))} eder.')

# sayı formatlama...
sayi = 123
print(f"{sayi:>6}") #'   123'

print(f"{sayi:0>+6}") #'00+123'

print(f"{sayi:0=+6}") #'+00123'

print(f"Binary: {sayi:b} | Octal: {sayi:o} | Hexadecimal: {sayi:x}") #'Binary: 1111011 | Octal: 173 | Hexadecimal: 7b'

print(f"Binary: {sayi:#b} | Octal: {sayi:#o} | Hexadecimal: {sayi:#x}") #'Binary: 0b1111011 | Octal: 0o173 | Hexadecimal: 0x7b'

ondalik = 0.123
print(f"{ondalik:.2f}") # f | F ondalık formatlama  '0.12'

print(f"{ondalik:.5f}") #'0.12300'

print(f"{ondalik:.5g}") # g | G fazla sıfırlar dahil edilmez  '0.123'

sayi = 123456
print(f"{sayi:_}") #'123_456'

print(f"{sayi:-^15_}") #'----123_456----'

print(f"{sayi:,}") #'123,456'

# Yüzde gösterimi
oran = 0.856
print(f"Başarı oranı: {oran:.1%}")  # 85.6%

islem = 1 / 12
print(f"{islem:.2%}") # Sonucun 100 ile çarpılmış halini yüzde olarak çıktı verir  '8.33%'

#
selam = "Hello, World!"
hizalama = {"Sol": "<", "Orta": "^", "Sağ": ">"}
genislik = 25
for hiza, operator in hizalama.items():
    print(f"{hiza:>5}: '{selam:{operator}{genislik}}'")
"""
 Sol: 'Hello, World!            '
Orta: '      Hello, World!      '
 Sağ: '            Hello, World!'
"""

# Hizalama
for urun, fiyat in [("Elma", 5), ("Portakal", 7.5), ("Muz", 12)]:
    print(f"{urun:<10} {fiyat:>6.2f} TL")
"""
Elma         5.00 TL
Portakal     7.50 TL
Muz         12.00 TL
"""
