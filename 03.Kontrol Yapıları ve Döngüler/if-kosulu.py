# koşul True olduğunda kod bloğu çalışır, False olduğunda kod bloğu çalışmaz.
# if <koşul>: 
#    <kod bloğu>

# if True:
#     print("kod bloğu...")
#
# if (False):
#     print("kod bloğu...")

###
kosul = (3 == 5)
if kosul:
    print("koşul sağlandığında çalışacak kod bloğu...")

###
login = False
if login:
    print("giriş başarılı...")

###
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

### Python koşulları yukarıdan aşağıya doğru sırayla kontrol eder. İlk True olan koşulun bloğu çalışır ve geri kalanlar atlanır.
not_ortalamasi = 79

if not_ortalamasi >= 90:
    harf = "AA"
elif not_ortalamasi >= 80:
    harf = "BA"
elif not_ortalamasi >= 70:
    harf = "BB"
elif not_ortalamasi >= 60:
    harf = "CB"
else:
    harf = "FF"

print(f"Harf notun: {harf}")  # Harf notun: BB


### Ternary Expression (Üçlü İfade)
# değer_true if koşul else değer_false
n = 7

# Klasik yol
if n > 0:
    sonuc = "pozitif"
else:
    sonuc = "negatif"

# Ternary yol
sonuc = "pozitif" if n > 0 else "negatif"
print(sonuc)  # pozitif


###
_not = 51
status = "Geçti" if _not > 50 else "Kaldı"
print(f"{status}")