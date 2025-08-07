a = b''
print(f"{a} => {type(a)}") #b'' => <class 'bytes'>

#Bayt veri tipi temel olarak ASCII karakterleri kabul eder. Dolayısıyla ASCII tablosu dışında kalan karakterleri doğrudan bayt olarak temsil edemezsiniz:
#a = b'ş' #hata!

#ASCII dışında kalan karakterleri de bayt’a dönüştürmek için bytes() adlı bir fonksiyon kullanılır:
b = bytes("ş", "utf-8") #yada b = "ş".encode("utf-8")
print(b) #b'\xc5\x9f'
b = str(b)[4:6]+str(b)[8:10]
print(b) #c59f sayısı utf-8 kod çözücünde 'ş' harfini temsil etmektedir.
b = int(b,16) #50591
print(bin(b)) #11000101:10011111
print(int("1100010110011111",2)) #50591
print(f"{b.bit_length()} bit.") #16 bit.

##
b = bytes("Fırat", "ascii", errors="xmlcharrefreplace")
print(b)


### Baytların Metotları
### decode() metodu baytları belli bir kodlama biçimine göre karakter dizilerine dönüştürebilmek için kullanılır.

d = b"\xc4\xb0".decode("utf-8")
print(d)