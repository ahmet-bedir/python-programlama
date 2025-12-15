###
class HarfSayaci:
    def __init__(self):
        self.sesli_harfler = 'aeıioöuü'
        self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
        self.sayac_sesli = 0
        self.sayac_sessiz = 0

    def kelime_sor(self):
        return input('Bir kelime girin: ')

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def sessizdir(self, harf):
        return harf in self.sessiz_harfler

    def artir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac_sesli += 1
            if self.sessizdir(harf):
                self.sayac_sessiz += 1
        return (self.sayac_sesli, self.sayac_sessiz)

    def ekrana_bas(self):
        sesli, sessiz = self.artir()
        mesaj = "'{}' kelimesinde {} sesli, {} sessiz harf var."
        print(mesaj.format(self.kelime, sesli, sessiz))

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == '__main__':
    sayaç = HarfSayacı()
    sayaç.çalıştır()
