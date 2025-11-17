### tek kullanımlık sınıf tanımlama.
class Calisan:
    kabiliyetleri = ["internet","tv"]
    unvani = 'işçi'

c1 = Calisan
print(c1.kabiliyetleri)
print(c1.unvani)

c2 = Calisan
print(c2.kabiliyetleri)
print(c2.unvani)

### yapıcı metod.
class Personal:
    def __init__(self):
        print("Yapıcı metod!")
        
nesne1 = Personal() # print ile yazdırmamamıza reğmen yapıcı metod çalışır.

