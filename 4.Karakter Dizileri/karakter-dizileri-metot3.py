### str.maketrans(), translate()
kaynak = "a"
hedef  = "A"

ceviri = str.maketrans(kaynak, hedef)
print(ceviri) #{97: 65} ascii tablosundaki harf : sayı karşılıkları.
#
kaynak = "şçöğüıŞÇÖĞÜİ"
hedef  = "scoguiSCOGUI"

ceviri_tablosu = str.maketrans(kaynak, hedef)

metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."
print(metin.translate(ceviri_tablosu))

#
metin = "Bfjflrk öa kdhsı yteua idjslyd bdcusldvdj ks?"

q_klavye_duzeni = "qwertyuıopğüasdfghjklşi,zxcvbnmöç."
f_klavye_duzeni = "fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"

ceviri_tablosu = str.maketrans(q_klavye_duzeni, f_klavye_duzeni)

print(metin.translate(ceviri_tablosu))

