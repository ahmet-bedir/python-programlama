###
tr_harfler = "çÇğĞıİöÖşŞüÜ"
parola = input("Parola Belirleyiniz : ")

for karakter in parola: #parola değişkenine girdiğimiz her karakteri tek tek karakter adlı değişkene attık.
    if karakter in tr_harfler: #karakter değişkenindeki her bir karakterin tr_harfler değişkenindeki karakterlerde olup olmadığına bakıyoruz.
        print("""Parolada Türkçe Karakter Kullanılamaz...
Lütfen Tekrar Deneyin!""")
        exit()
    
print("""Parolanız Başarılı Bir Şekilde Oluşturulmuştur...
Parolanız :""", parola)

###
tr_harfler = "çÇğĞıİöÖşŞüÜ"
while True:
  parola = input("Parola Belirleyiniz : ")
  for karakter in parola:
      if karakter in tr_harfler:
          print("Parolada Türkçe Karakter Kullanılamaz...")
          break
  else:
      print("Parolanız :", parola)
      break

###
while True:
    parola = input("Parola Belirleyiniz : ")
    if ' ' in parola:
        print("Parolanızda Boşluk Olmamalı.!")
    elif len(parola) in range(3, 9): #eğer parolanızın uzunluğu 2 ile 9 karakter aralığında ise...
        print("Parolalanız :", parola)
        break
    else:
        print("Parola 8 Karakterden Uzun, 3 Karakterden Kısa Olmamalı...")

### Karakter Dizilerinin İçeriğini Karşılaştırma.
metin1 = "123451234589"
metin2 = "135797979"
fark = ""

#metin1 adlı değişken içinde bulunan, ama metin2 adlı değişken içinde bulunmayan öğeleri ayırma...
for m1 in metin1: #metin1'deki bütün öğeleri 'm1' adını verdiğimiz değişkene verdik...
    if m1 not in metin2: #eğer 'm1' adlı bu öğe metin2'de yoksa...
        if not m1 in fark: #eğer 'm1' adlı bu öğe fark'dada yoksa 'fark' değişkenini ekrana bas...
            fark += m1
print(*fark)

#for m1 in metin1:
   #if not m1 in metin2 and not m1 in fark:
        #fark += m1
#print(*fark)

#### dosya içeriklerini karşılaştırıp, farklı öğeleri ortaya sermek.
d1 = open("isimler1.txt") # dosyayı açıyoruz
d1_satırlar = d1.readlines() # satırları okuyoruz

d2 = open("isimler2.txt")
d2_satırlar = d2.readlines()

for i in d2_satırlar:
    if not i in d1_satırlar:
        print(i)

d1.close()
d2.close()

####
metin = """Bu programlama dili Guido
Van Rossum adlı Hollandalı bir 
programcı tarafından 90’lı yılların 
başında geliştirilmeye başlanmıştır..."""
g = input("Sorgulamak İsrediğiniz Harfi Giriniz : ")
harf = ''
for i in metin: #metin içindeki her bir öğeyi 'i' değişkenine at
    if i == g: #i eşitse girilen harfe...
        harf += i #harfe i'yi ekle
print(g, "harfi metinde", len(harf),
"kere geçiyor...")

#### metindeki her bir karakteri bir kere ekrana yaz...
metin = "python programlama dili..."

harf = ''
for i in metin:
    if i in metin and i not in harf:
        harf += i
print(*harf)