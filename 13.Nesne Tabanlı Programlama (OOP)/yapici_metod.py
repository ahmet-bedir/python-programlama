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


ornek1 = Deneme()
print(ornek1.a, ornek1.b)