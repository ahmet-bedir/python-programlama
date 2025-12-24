import re
liste = ["özcan deniz", "1mehmet", "85süleyman", "selim", "kemal", "özkan", "esra", "05dündar", "esin", "esma4", "özhan", "öz9lem", "özkan"]
# for l in liste:
#     sorgu = re.search("öz[kch]an", l)
#     if sorgu:
#         print(sorgu.group())

## sayı ile başlayanlar listelendi.
for l in liste:
    if re.match("[0-9]", l):
        print(l)