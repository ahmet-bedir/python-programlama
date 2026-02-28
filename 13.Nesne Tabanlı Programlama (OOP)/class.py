class Person:
	def __init__(self, name):
		self.name = name
		print("Yapıcı Metod (constructor metod) Çalıştı.")

object1 = Person("ali")
print(object1.name)

object2 = Person("aylin")
print(object2.name)