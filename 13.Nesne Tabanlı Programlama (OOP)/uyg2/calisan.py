class Calisan:
    personel = []
    def __init__(self,isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personel_ekle()

    def personel_ekle(self):
        self.personel.append(self.isim)
        print(f"'{self.isim}' adlı kişi personel listesine eklendi.")

    @classmethod
    def personel_listesi(cls):
        print("=== Personel Listesi ===")
        for kisi in cls.personel:
            print(kisi)

    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
        
    def kabiliyet_listesi(self):
        print(f"'{self.isim}' adlı personelin kabiliyetleri:")
        for k in self.kabiliyetleri:
            print(k)

    @classmethod
    def personel_sayisi(cls):
        print(f"Personel Sayısı: {len(cls.personel)}")
        
        
'''
class Sınıf():
    sınıf_niteliği = 0

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        self.örnek_niteliği = 0

    def örnek_metodu(self):
        self.örnek_niteliği += 1
        return self.örnek_niteliği

    @classmethod
    def sınıf_metodu(cls):
        cls.sınıf_niteliği += 1
        return cls.sınıf_niteliği
'''
