class Calisan:
    __personel = []
    def __init__(self,isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personel_ekle()

    def personel_ekle(self):
        self.__personel.append(self.isim)
        print(f"'{self.isim}' adlı kişi personel listesine eklendi.")

    @classmethod
    def personel_listesi(cls):
        print("=== Personel Listesi ===")
        for kisi in cls.__personel:
            print(kisi)

    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
        
    def kabiliyet_listesi(self):
        print(f"'{self.isim}' adlı personelin kabiliyetleri:")
        for k in self.kabiliyetleri:
            print(k)

    @classmethod
    def personel_sayisi(cls):
        print(f"Personel Sayısı: {len(cls.__personel)}")