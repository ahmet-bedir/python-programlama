x = 2
y = 3.35
metin = "True"
mantiksal = False

print("Başlangıç Tip Değerleri")
print("x :", x, type(x))
print("y :", y, type(y))
print("metin :", metin, type(metin))
print("mantıksal :", mantiksal, type(mantiksal))

print("int => float")
x = float(x)
print("x :", x, type(x))

print("float => int")
y = int(y)
print("y :", y, type(y))

print("float int => str")
s = str(x) + str(y)
print("x + y :", s, type(s))

print("bool => int")
m = int(mantiksal)
print("mantıksal :", m, type(m))

print("str => bool")
s = bool(metin)
print("metin :", s, type(s))
