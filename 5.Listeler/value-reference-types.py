# değer tipler (value types) : bellekte değer olarak tutulur.
x = 10
y = 20
x = y
y = 30
print("x :", x)
print("y :", y)

# referans tipler (reference types) : bellekte adres olarak tutulur.
liste1 = [1,2,3]
liste2 = [4,5,6]
liste1 = liste2
liste1[0] = 11
print("liste1 :", liste1)
print("liste2 :", liste2)

# liste kopyalama (değer tip)
listeA = [1,2,3]
listeB = listeA.copy()
listeA[0] = 11
print("listeA :", listeA)
print("listeB :", listeB)