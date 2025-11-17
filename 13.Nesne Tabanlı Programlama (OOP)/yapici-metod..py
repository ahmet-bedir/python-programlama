### yapıcı metod.
#class Personal:
#   def __init__(self):
#      print("Yapıcı metod!")
#nesne1 = Personal() # sınıfın örneklendiği an yapıcı metod çalışır.
"""
###
class Urunler:
    def __init__(self, adi, fiyat, durum):
        self.urun_adi = adi
        self.urun_fiyat = fiyat
        self.aktifmi = durum
    def kdv(self):
        return self.urun_fiyat*0.5
    def bilgi(self):
        print(f"Ürün Adı: {self.urun_adi}\nFiyatı {self.urun_fiyat}\nKDV: {self.kdv()}", end="\n\n")


urun1 = Urunler("telefon", 8000, True)
urun2 = Urunler("laptop", 20000, True)
urun3 = Urunler("tv", 28000, False)
urun4 = Urunler("lcd", 18000, True)

urun_listesi = [urun1,urun2,urun3,urun4]

for urun in urun_listesi:
    if urun.aktifmi:
        print(urun.bilgi())
        
"""


