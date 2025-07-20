###
a = 5

def func():
    print("local alandaki a =", a)
    
func()
print("global alandaki a =", a)

###
a = 5

def func():
    a = 3
    print("local alandaki a =", a)
    
func()
print("global alandaki a =", a)

###
def func():
    global sayi
    sayi = 7
    
func()
print("fonksiyonun içindeki sayi =", sayi)