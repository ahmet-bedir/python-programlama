class Calisan:
    personel = []
    def __init__(self,isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personel_ekle()

    def personel_ekle(self):
        self.personel.append(self.isim)
        print(f"'{self.isim}' adlı kişi personel listesine eklendi.")

    def personel_listesi(self):
        print("== Personel Listesi ==")
        for kisi in self.personel:
            print(kisi)

    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
        
    def kabiliyet_listesi(self):
        print(f"'{self.isim}' adlı personelin kabiliyetleri:")
        for k in self.kabiliyetleri:
            print(k)
