class Calisan:
    personel = []
    def __init__(self,isim):
        self.isim = isim
        self.personel_ekle()
    def personel_ekle(self):
        self.personel.append(self.isim)
        print(f"'{self.isim}' adlı kişi personel listesine eklendi.")
