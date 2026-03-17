### yapıcı metod.
class Personal:
  def __init__(self):
     print("Yapıcı metod!")

nesne1 = Personal() # sınıfın örneklendiği an yapıcı metod çalışır.

###
class Deneme:
    a = 5
    def __init__(self):
        self.b = 7

print("Sınıf niteliği:", Deneme.a)

# 1.yöntem
ornek1 = Deneme()
print("Örnek niteliği:", ornek1.b)

# 2.yöntem
print("Örnek niteliği:", Deneme().b)