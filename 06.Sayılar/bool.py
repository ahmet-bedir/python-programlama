print(isinstance(True, int))   # True — bool, int'in alt sınıfı
print(True == 1)    # True
print(False == 0)   # True

# Aritmetik işlemlerde kullanılabilir
print(True + True)        # 2
print(True + False)       # 1
print(True * 10)          # 10
print(False * 10)         # 0

# Sayma trick'i — True'ları say
sayilar = [3, 7, 2, 9, 1, 8, 4]
buyuk_sayisi = sum(x > 5 for x in sayilar)
print(f"5'ten büyük: {buyuk_sayisi}")  # 3 (Bu, her True bir 1 olduğu için çalışır. sum() içinde her True 1 olarak toplanır)


################
# Pratik: doğru cevap yüzdesi
cevaplar = [True, False, True, True]
basari_orani = sum(cevaplar) / len(cevaplar)
print(f"Başarı: {basari_orani:.0%}")  # Başarı: 75%

################
# Bu değerlerin hepsi False olarak değerlendirilir
falsy_degerler = [
    False,      # bool False
    0,          # sıfır (int)
    0.0,        # sıfır (float)
    0j,         # sıfır (complex)
    "",         # boş string
    [],         # boş liste
    (),         # boş tuple
    {},         # boş dict
    set(),      # boş set
    None,       # None
    range(0),   # boş range
]

for deger in falsy_degerler:
    print(f"bool({str(deger)}) = {bool(deger)}")
    
# Bunların hepsi True olarak değerlendirilir
truthy_degerler = [
    True,           # bool True
    1,              # sıfır olmayan int
    -1,             # negatif sayılar da truthy
    3.14,           # sıfır olmayan float
    "merhaba",      # dolu string
    " ",            # boşluk bile truthy (boş değil çünkü)
    [1, 2],         # dolu liste
    {"a": 1},       # dolu dict
    (0,),           # dolu tuple (içi 0 olsa bile)
]

for deger in truthy_degerler:
    print(f"bool({str(deger):15s}) = {bool(deger)}")
    
    
###
# ❌ Gereksiz karşılaştırma
if len(liste) > 0:
    print("Liste dolu")

if aktif == True:
    print("Aktif")

if isim != "":
    print("İsim var")

# ✅ Pythonic yol
if liste:
    print("Liste dolu")

if aktif:
    print("Aktif")

if isim:
    print("İsim var")
    
# Boş kontrolleri
def kullanici_bilgi(isim, email=None, telefon=None):
    print(f"İsim: {isim}")
    
    if email:
        print(f"E-posta: {email}")
    else:
        print("E-posta belirtilmemiş")
    
    if telefon:
        print(f"Telefon: {telefon}")
    else:
        print("Telefon belirtilmemiş")

kullanici_bilgi("Ali", email="ali@test.com")
# İsim: Ali
# E-posta: ali@test.com
# Telefon belirtilmemiş


# int ve float karşılaştırılabilir
print(1 == 1.0)     # True
print(1 < 1.5)      # True

# bool ve int karşılaştırılabilir (bool, int'in alt sınıfı)
print(True == 1)    # True
print(False == 0)   # True

# String karşılaştırma — leksikografik (Unicode sırasına göre)
print("apple" < "banana")   # True
print("abc" < "abd")        # True
print("A" < "a")            # True (A=65, a=97)

# Farklı tipler karşılaştırılamaz (< , > için)
# print("5" < 5)  # TypeError!
print("5" == 5)    # False — hata vermez ama False döner

###
def giris_kontrol(kullanici_adi, sifre, aktif_mi):
    if not kullanici_adi or not sifre:
        return "Kullanıcı adı ve şifre gerekli!"
    
    if not aktif_mi:
        return "Hesabınız aktif değil!"
    
    if len(sifre) < 8:
        return "Şifre en az 8 karakter olmalı!"
    
    return "Giriş başarılı!"

print(giris_kontrol("ali", "12345678", True))   # Giriş başarılı!
print(giris_kontrol("", "12345678", True))        # Kullanıcı adı ve şifre gerekli!
print(giris_kontrol("ali", "123", True))          # Şifre en az 8 karakter olmalı!
print(giris_kontrol("ali", "12345678", False))    # Hesabınız aktif değil!

#######################
# and operatöründe ilk değer False ise, ikinci değere bakmaya gerek yok — sonuç zaten False.
# İlk koşul False → ikinci koşul hiç çalışmaz
x = 0
if x != 0 and 10 / x > 2:  # 10/0 hatası olmaz!
    print("Koşul sağlandı")
else:
    print("x sıfır")  # Bu çalışır

# Güvenli erişim deseni
liste = []
if liste and liste[0] > 5:  # Boş liste → IndexError olmaz!
    print("İlk eleman 5'ten büyük")
    
# or operatöründe ilk değer True ise, ikinci değere bakmaya gerek yok — sonuç zaten True
# İlk koşul True → ikinci koşul hiç çalışmaz
x = 10
if x > 5 or cok_pahali_fonksiyon():  # Bu fonksiyon çağrılmaz!
    print("Koşul sağlandı")
    
##############
# Varsayılan Değer Deseni
# or operatörünün bu davranışı, varsayılan değer atamak için kullanılır:
# Kullanıcı isim girmemişse varsayılan kullan
isim = input("İsminiz: ") or "Anonim"

print(isim)

##############
# Fonksiyon parametrelerinde
def selamla(isim=None):
    isim = isim or "Dünya"
    return f"Merhaba, {isim}!"

print(selamla())         # Merhaba, Dünya!
print(selamla("Ali"))    # Merhaba, Ali!

##############
### 