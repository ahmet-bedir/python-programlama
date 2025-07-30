kod_sayfalari = ["ascii","utf-8"]
harfler = "abcçdefghijklmnoprstuvyz"

print('+'+('-'*32)+'+')
print("|{:<10}|{:<10}|{:<10}|".format("karakter", kod_sayfalari[0], kod_sayfalari[1]))
print('+'+('-'*32)+'+')
for kd in kod_sayfalari:
    for harf in harfler:
        print("|{:<10}|{:<10}|{:<10}|".format(harf, str(len(harf.encode(kd,errors="ignore")))+'p bayt', str(len(harf.encode(kd)))+' bayt'))
print('+'+('-'*32)+'+')

"""
kod_çözücüler = ['UTF-8', 'cp1254', 'latin-1', 'ASCII']

harf = 'a'

for kç in kod_çözücüler:
    try:
        print("'{}' karakteri {} ile {} olarak " "ve {} sayısıyla temsil edilir.".format(harf, kç, harf.encode(kç),ord(harf)))
    except UnicodeEncodeError:
        print("'{}' karakteri {} ile temsil edilemez!".format(harf, kç))
"""