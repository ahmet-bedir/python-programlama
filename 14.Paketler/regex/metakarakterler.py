import re

### [] metakarakteri içinde gördüğü bütün karakterleri tek tek liste öğelerine uyguluyor. Önce “öz” ile başlayan bütün öğeleri alıyor, ardından “öz” hecesinden sonra “c” harﬁyle devam eden ve “an” hecesi ile biten öğeyi buluyor. Böylec “özcan” öğesini bulmuş oldu. Aynı işlemi, “öz” hecesinden sonra “h” harﬁni barındıran ve “an” hecesiyle biten öğeye uyguluyor. Bu şekilde ise “özhan” öğesini bulmuş oldu. En son hedef ise “öz” ile başlayıp “k” harﬁ ile devam eden ve “an” ile biten öğe. Yani listedeki “özkan” öğesi. En nihayetinde de elimizde “özcan”, “özhan” ve “özkan” öğeleri kalmış oluyor.
liste = ["özcan", "mehmet", "süleyman", "selim", "ahmet", "özkan", "esra", "dündar", "esin", "esma", "özhan", "özlem", "özkan"]
# for l in liste:
#     sorgu = re.search("öz[kch]an", l)
#     if sorgu:
#         print(sorgu.group())
#
# print("-"*35)
# for l in liste:
#     if re.search("es[mr]a",l):
#         print(l)

## sayı ile başlayanları listelemek için:
# liste = ["23BH56","Ty76Z","4Y7UZ","TYUDZ","34534"]
# for l in liste:
#     if re.match("[0-9]", l):
#         print(l) # 23BH56 4Y7UZ 34534

# Düzenli ifademiz içinde geçen birinci [A-Z] ifadesi aradığımız karakter dizisi olan “Ty76Z” içindeki “T” harﬁni, ikinci [a-z] ifadesi “y” harﬁni, [0-9] ifadesi ise “7” sayısını temsil ediyor. Karakter dizisi içindeki geri kalan harﬂer ve sayılar otomatik olarak eşleştirilecektir. Listeden sadece “Ty76Z” öğesini alır.
# for l in liste:
#     if re.match("[A-Z][a-z][0-9]",l):
#         print(l)

### . (nokta) metakarakteri, yeni satır karakteri hariç bütün karakterleri temsil etmek için kullanılır. “.” metakarakteri sadece tek bir karakterin yerini tutuyor.
# for l in liste:
#     sorgu = re.match("es.a",l)
#     if sorgu:
#         print(sorgu.group())


#
# a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ', '34534', "1agAY54"]
# for i in a:
#     if re.match(".[0-9a-z]", i):
#         print(i)
"""
1. Herhangi bir karakter ile başlayacak. Bu karakter sayı, harf veya başka bir karakter
olabilir.
2. Ardından bir sayı veya alfabedeki küçük harﬂerden herhangi birisi gelecek.
3. Bu ölçütleri karşıladıktan sonra, aradığımız karakter dizisi herhangi bir karakter ile
devam edebilir.
çıktı:
23BH56
34534
1agAY54
"""

### * (Yıldız) metakarakteri, kendinden önce gelen bir düzenli ifade kalıbını sıfır veya daha fazla sayıda eşleştirir.
# yeniliste = ["st", "sat", "saat", "saaat", "falanca"]
# for i in yeniliste:
#     if re.match("sa*t",i):
#         print(i)
"""
Burada “*” sembolü kendinden önce gelen “a” karakterini sıfır veya daha fazla sayıda eşleştiriyor. Yani mesela “st” içinde sıfır adet “a” karakteri var. Dolayısıyla bu karakter yazdığımız düzenli ifadeyle eşleşiyor. “sat” içinde bir adet “a” karakteri var. Dolayısıyla bu da eşleşiyor. “saat” ve “saaat” karakter dizilerinde sırasıyla iki ve üç adet “a” karakteri var. Tabii ki bunlar da yazdığımız düzenli ifadeyle eşleşiyor. Listemizin en son öğesi olan “falanca”da da ilk hecede bir adet “a” karakteri var. Ama bu öğedeki sorun, bunun “s” harﬁyle başlamaması.
"""

for l in liste:
    if re.match(".*met",l):
        print(l)