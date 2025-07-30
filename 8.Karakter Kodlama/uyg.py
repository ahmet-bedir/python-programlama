kod_sayfalari = ["ASCII ","utf-8","cp1254"]
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"

print('+'+('-'*43)+'+')
print("|{:<10}|{:<10}|{:<10}|{:<10}|".format("karakter", kod_sayfalari[0], kod_sayfalari[1], kod_sayfalari[2]))
print('+'+('-'*43)+'+')

for harf in harfler:
   print("|{:<10}|{:<10}|{:<10}|{:<10}|".format(harf, len(harf.encode(kod_sayfalari[0],errors="ignore")), len(harf.encode(kod_sayfalari[1])), len(harf.encode(kod_sayfalari[2]))))
print('+'+('-'*43)+'+')


"""
kod_çözücüler = ['UTF-8', 'cp1254', 'latin-1', 'ASCII']

harf = 'a'

for kç in kod_çözücüler:
    try:
        print("'{}' karakteri {} ile {} olarak " "ve {} sayısıyla temsil edilir.".format(harf, kç, harf.encode(kç),ord(harf)))
    except UnicodeEncodeError:
        print("'{}' karakteri {} ile temsil edilemez!".format(harf, kç))
"""