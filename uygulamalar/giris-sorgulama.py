s1 = input("1.sayı: ")
s2 = input("2.sayı: ")

if s1 > s2:
    print("{} x {} = {}".format(s1,s2,int(s1)*int(s2)))
else:
    print("{} + {} = {}".format(s1,s2,int(s1)+int(s2)))