### kabiliyetleri listesine ekleme yaptığımızda, bu durum o sınıfın bütün örneklerini etkiliyor yani tek kullanımlık sınıf tanımlamış oluyor.
class Calisan:
    kabiliyetleri = []
        
###
class Calisan:
    a = 4
    def __init__(self):
        self.kabiliyetleri = []


ahmet = Calisan()
ahmet.kabiliyetleri.append("bilgisayar")
ahmet.kabiliyetleri.append("yazılım")

print(f"Ahmet: {ahmet.kabiliyetleri}")


mehmet = Calisan()
mehmet.kabiliyetleri.append("konuşkan")

print(f"Mehmet: {mehmet.kabiliyetleri}")
