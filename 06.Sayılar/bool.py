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
    
