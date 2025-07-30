for i in range(1, 5):
    print("{} bayt kullanırsak toplam 2**{:<2} = {:,} karakter kodlanabilinir.".format(i, i*8, (2**(i*8))))
    
    
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
for s in harfler:
    print("{:<5}{:<15}{} bayt".format(s,str(s.encode("utf-8")), len(s.encode("utf-8"))))