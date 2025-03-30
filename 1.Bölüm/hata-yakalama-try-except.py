'''
try:
    ...hata verebileceğini bildiğimiz kodlar...
except HataAdı:
    ...hata durumunda yapılacak işlem...
'''
while True:
    sayi1 = input("1.sayı (çıkış : q) : ")
    if sayi1 == 'q':
        break
    sayi2 = input("2.sayı : ")
    try:
        sayi1 = int(sayi1)
        sayi2 = int(sayi2)
        print("Bölme İşleminin Sonucu :", sayi1/sayi2)
    #except ValueError:
        #print("Lütfen Sayı Giriniz!")
    #except ZeroDivisionError:
        #print("Sıfıra Bölünme Hatası!")
    #except (ValueError, ZeroDivisionError): #hata türlerini grupladık.
    	#print("Bir Hata Oluştu!")
    	
    #except ValueError as hata:
    	#print("Lütfen Sayı Giriniz!")
    	#print("Hata açıklaması :", hata)
    #except ZeroDivisionError as hata:
    	#print("Sıfıra Bölünme Hatası!")
    	#print("Hata açıklaması :", hata)
    except (ValueError, ZeroDivisionError) as hata:
        print("Bir Hata Oluştu!")
        print("Hata açıklaması :", hata)
'''
Her hata için ayrı bir mesaj göstermek en iyisidir. Ama tabii dilerseniz hata türlerini gruplayıp hepsi için tek bir hata mesajı göstermeyi de tercih edebilirsiniz.
'''
###
try:
    bolunen = int(input("bölünecek sayı: "))
    bolen = int(input("bölen sayı: "))
except ValueError:
    print("Lütfen sadece sayı girin!")
else:
    try:
        print(bolunen/bolen)
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz!")
'''
try:
    ...bir takım işler...
except birHata:
    ...hata alınınca yapılacak işlemler...
finally:
    ...hata olsa da olmasa da yapılması gerekenler...
'''
###
try:
    dosya = open("dosyaadı", "r")
    ...burada dosyayla bazı işlemler yapıyoruz...
    ...ve ansızın bir hata oluşuyor...
except IOError:
    print("Bir Hata Oluştu!")
finally:
    dosya.close()
'''
Kullanıcının yaptığı bir işlem normal şartlar altında hata vermeyecek olsa bile biz ona ‘Python tarzı’ bir hata mesajı göstermek için raise deyimini kullanıyoruz.
'''
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

'''
raise deyimini, bir hata mesajına ek olarak bir işlem yapmak istediğimizde de kullanabiliriz.
'''
###
try:
    bolunen = 7
    bolen = 0
    print(bolunen/bolen)
except ZeroDivisionError:
    print("bir sayıyı 0'a bölemezsiniz!")
    raise

####

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
