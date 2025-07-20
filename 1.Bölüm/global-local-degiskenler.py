###
a = 5

def func():
    print("fonksiyonun içindeki a =", a)
    
func()
print("global alandaki a =", a)

###
a = 5

def func():
    a = 3
    print("fonksiyonun içindeki a =", a)
    
func()
print("global alandaki a =", a)

###
def func():
    global sayi
    sayi = 7
    
func()
print("fonksiyonun içindeki sayi =", sayi)