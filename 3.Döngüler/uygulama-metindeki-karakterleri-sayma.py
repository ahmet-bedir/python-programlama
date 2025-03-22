### Karakter Dizisindeki Girilen Karakteri Sayma
metin = """Bu programlama dili Guido
Van Rossum adlı Hollandalı bir 
programcı tarafından 90’lı yılların 
başında geliştirilmeye başlanmıştır..."""
print(metin)
giris = input("Sorgulamak isrediğiniz harfi giriniz : ")
harf_sayisi = 0

for harf in metin: #metin içindeki her bir öğeyi 'harf' değişkenine yolla.
    if harf == giris: #harf değişkeni eşitse girilen harfe...
        harf_sayisi += 1 #harf_sayisi değişkenini bir arttır.
print("'{}' harfi metinde {} kere geçiyor...".format(giris, harf_sayisi))

### 2.yöntem
metin = """Bu programlama dili Guido
Van Rossum adlı Hollandalı bir 
programcı tarafından 90’lı yılların 
başında geliştirilmeye başlanmıştır..."""
print(metin)
giris = input("Sorgulamak isrediğiniz harfi giriniz : ")
harf_sayisi = ''

for harf in metin: #metin içindeki her bir öğeyi 'harf' değişkenine yolla.
    if harf == giris: #harf değişkeni eşitse girilen harfe...
        harf_sayisi += harf #harf_sayisi değişkenine harfi ekle.
print("'{}' harfi metinde {} kere geçiyor...".format(giris, len(harf_sayisi)))