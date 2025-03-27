"""

#except (ValueError, ZeroDivisionError):

#except ValueError as hata:
    #print("Hata Açıklaması : ", hata)
#except ValueError as hata:
    #print("Sadece sayı girin!")
    #print("Orijinal hata mesajı: ", hata)
    
#except (ValueError, ZeroDivisionError) as hata:
    #print("Bir hata oluştu!")
    #print("Orijinal hata mesajı: ", hata)

###
while True:
    ilk_sayi = input("ilk sayı (Programdan çıkmak için q tuşuna basın): ")

    if ilk_sayi == "q":
        break

    ikinci_sayi = input("ikinci sayı: ")

    try:
        sayi1 = int(ilk_sayi)
        sayi2 = int(ikinci_sayi)
        print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
    except (ValueError, ZeroDivisionError):
        print("Bir hata oluştu!")
        print("Lütfen tekrar deneyin!")

###
try:
    dosya = open("dosyaadı", "r")
    ...burada dosyayla bazı işlemler yapıyoruz...
    ...ve ansızın bir hata oluşuyor...
except IOError:
    print("bir hata oluştu!")
finally:
    dosya.close()

###
bolunen = int(input("bölünecek sayı: "))

if bolunen == 23:
    raise Exception("Bu programda 23 sayısını görmek istemiyorum!")

bolen = int(input("bölen sayı: "))
print(bolunen/bolen)

###
tr_karakter = "şçğüöıİ"

parola = input("Parolanız: ")

for i in parola:
    if i in tr_karakter:
        raise TypeError("Parolada Türkçe karakter kullanılamaz!")
    else:
        pass

print("Parola kabul edildi!")

###
try:
    bölünen = 6
    bölen = 6
    print(bölünen/bölen)
except ZeroDivisionError:
    print("bir sayıyı 0'a bölemezsiniz")
    raise

####
giris = ""
if len(giris) == 0:
    raise AssertionError("İsim bölümü boş.")
print("Hoşgeldiniz.")
"""
####
giris = " "
assert len(giris) != 0 , "İsim bölümü boş."
print("Hoşgeldiniz.")

# bütün hatalar için
try:
    birtakım kodlar
except ValueError:
    print("Yanlış değer")
except ZeroDivisionError:
    print("Sıfıra bölme hatası")
except:
    print("Beklenmeyen bir hata oluştu!")
