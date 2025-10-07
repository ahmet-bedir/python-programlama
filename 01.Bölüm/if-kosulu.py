"""
if <koşul>: #koşul True olduğunda kod bloğu çalışır, False olduğunda kod bloğu çalışmaz.
    <kod bloğu>
"""
# if True:
#     print("kod bloğu...")
#
# if (False):
#     print("kod bloğu...")

#
kosul = (3 == 5)
if kosul:
    print("koşul sağlandığında çalışacak kod bloğu...")

login = False
if login:
    print("giriş başarılı...")

email = "info@gmail.com"
parola = "123"
login = (email == "inf@gmail.com") and (parola == "123")
if login:
    print("giriş başarılı...")

### verimsiz yöntem, çünkü 10'un altında bir değer girilmesi durumunda hem birinci hem ikinci if bloğu çalışır.
# print("ilk yöntem.")
# sayi = int(input("Sayı Giriniz : "))
#
# if sayi < 10:
#     print("sayı 10'dan küçüktür.")
#
# if sayi < 20:
#     print("sayı 20'den küçüktür.")
#
# if sayi > 20:
#     print("sayı 20'den büyüktür.")
#
# if sayi > 30:
#     print("sayı 30'dan büyüktür.")
#
### if bize olası bütün sonuçları listeler, elif ise sadece doğru olan ilk sonucu verir.
# print("ikinci yöntem.")
# sayi = int(input("Sayı Giriniz : "))
#
# if sayi < 10:
#     print("sayı 10'dan küçüktür.")
# elif sayi < 20:
#     print("sayı 20'den küçüktür.")
# elif sayi > 30:
#     print("sayı 30'dan büyüktür.")
# elif sayi > 20:
#     print("sayı 20'den büyüktür.")
#