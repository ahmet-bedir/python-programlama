### str.maketrans(), translate()
kaynak = "a"
hedef  = "A"

ceviri = str.maketrans(kaynak, hedef)
print(ceviri) #{97: 65} ascii tablosundaki sayı karşılıkları.
#
kaynak = "şçöğüıŞÇÖĞÜİ"
hedef  = "scoguiSCOGUI"

ceviri_tablosu = str.maketrans(kaynak, hedef)

metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."
print(metin.translate(ceviri_tablosu))

#Türkçe-F klavye düzeni ile yazılmış metni, Türkçe-Q kavye düzenine çevirme.
metin = "Bfjflrk öa kdhsı yteua idjslyd bdcusldvdj ks?"

q_klavye_duzeni = "qwertyuıopğüasdfghjklşi,zxcvbnmöç."
f_klavye_duzeni = "fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"

ceviri_tablosu = str.maketrans(q_klavye_duzeni, f_klavye_duzeni)

print(metin.translate(ceviri_tablosu))

#metinde bulunan bütün sesli harflerin silinmesi.
metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir
programcı tarafından 90'lı yılların başında geliştirilmeye başlanmıştır.
Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını
piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu
programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty
Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak
her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır
diyebiliriz."""

sesli_harfler = "aeıioöuüAEIİOÖUÜ"

yeni_metin = ""

for i in metin:
    if not i in sesli_harfler:
        yeni_metin += i

print(yeni_metin)

#
metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir
programcı tarafından 90'lı yılların başında geliştirilmeye başlanmıştır.
Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını
piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu
programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty
Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak
her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır
diyebiliriz."""

silinecek = "aeıioöuüAEIİOÖUÜ"

ceviri = str.maketrans('','',silinecek)

print(metin.translate(ceviri))
