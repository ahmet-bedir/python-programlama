###
'''
class Personal:
    def __init__(self):
        print("Yapıcı metod!")
        
nesne1 = Personal()
'''

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
