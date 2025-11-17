###
'''
class Personal:
    def __init__(self):
        print("Yapıcı metod!")
        
nesne1 = Personal()


###
class Personal:
    def __init__(self,a,y):
        self.ad = a
        self.yas = y
        
p1 = Personal("ahmet",37)
p2 = Personal("ali",27)
p3 = Personal("mehmet",18)

print(p1.ad, '-', p1.yas)
print(p3.ad, '-', p3.yas)


###
class Personal:
    def __init__(self,a,y):
        self.ad = a
        self.yas = y
    def __str__(self):
        return f"Kullanıcı Gözüyle:\nİsim : {self.ad}\nYaş : {self.yas}"
    def __repr__(self):
        return f"Yazılımcı Gözüyle:\nİsim : {self.ad!r}\nYaş : {self.yas!r}"
        
p1 = Personal("ahmet",37)
p2 = Personal("ali",27)
p3 = Personal("mehmet",18)

print(repr(p1))
print(p2)
print(p3)
'''
"""
###
class HarfSayacı:
    def __init__(self):
        self.sesli_harfler = 'aeıioöuü'
        self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
        self.sayaç_sesli = 0
        self.sayaç_sessiz = 0

    def kelime_sor(self):
        return input('Bir kelime girin: ')

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def sessizdir(self, harf):
        return harf in self.sessiz_harfler

    def artır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayaç_sesli += 1
            if self.sessizdir(harf):
                self.sayaç_sessiz += 1
        return (self.sayaç_sesli, self.sayaç_sessiz)

    def ekrana_bas(self):
        sesli, sessiz = self.artır()
        mesaj = "'{}' kelimesinde {} sesli, {} sessiz harf var."
        print(mesaj.format(self.kelime, sesli, sessiz))

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == '__main__':
    sayaç = HarfSayacı()
    sayaç.çalıştır()
"""

###
