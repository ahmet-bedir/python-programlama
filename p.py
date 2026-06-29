import math

sayilar = [2, 5, 10, 15, 20, 25, 30]

# Walrus olmadan
sonuclar = []
for s in sayilar:
    kok = math.sqrt(s)
    if kok > 3:
        sonuclar.append(kok)
        print(sonuclar)