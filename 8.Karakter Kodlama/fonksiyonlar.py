#Python programlama dilinde nesneler iki farklı şekilde temsil edilir:
#1.Python’ın göreceği şekilde
#2.Kullanıcının göreceği şekilde
#repr() fonsiyonuda pythonun bakış açısını yansıtır.
print("Python\n")

print(repr("Python\n"))

print('-'*47)

a = "elma "

print("{} kilo {} kaldı!".format(13,a)) #Gördüğünüz gibi, “elma” karakter dizisinin sol tarafında bir boşluk olduğu için ‘elma’ ile ‘kaldı’ kelimeleri arasında gereksiz bir açıklık meydana geldi. Bu boşluğu print() ile göremiyoruz, ama bu değişkeni repr() fonsiyonu ile kontol edebiliriz:
print(repr(a))
print("{} kilo {} kaldı!".format(13,a.strip()))


