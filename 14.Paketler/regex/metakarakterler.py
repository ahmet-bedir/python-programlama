import re
liste = ["özcan deniz", "1mehmet", "85süleyman", "selim", "kemal", "özkan", "esra", "05dündar", "esin", "esma4", "özhan", "öz9lem", "özkan", "gR123"]
# for l in liste:
#     sorgu = re.search("öz[kch]an", l)
#     if sorgu:
#         print(sorgu.group())

## sayı ile başlayanlar listelendi.
# for l in liste:
#     if re.match("[0-9]", l):
#     if re.match("[a-z][A-Z][0-9]",l):
#         print(l)

## . metakarakteri, yeni satır karakteri hariç bütün karakterleri temsil etmek için kullanılır.
for l in liste:
    sorgu = re.search("es.a",l)
    if sorgu:
        print(sorgu.group())
