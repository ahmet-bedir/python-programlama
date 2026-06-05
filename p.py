##############
# Bir fonksiyon açıkça return ifadesi kullanmazsa veya return tek başına kullanılırsa, None döner.
def selamla(isim):
    print(f"Merhaba, {isim}!")
    # return yok → None döner

sonuc = selamla("Ali")
print(sonuc)       # None
print(type(sonuc)) # <class 'NoneType'>