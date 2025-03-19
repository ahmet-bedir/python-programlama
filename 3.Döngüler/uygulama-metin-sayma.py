###
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