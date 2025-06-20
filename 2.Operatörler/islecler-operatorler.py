########################
# 1.Aritmetik İşleçler #
# +   toplama          #
# -   çıkarma          #
# *   çarpma           #
# /   bölme            #
# **  kuvvet alma      #
# %   modülüs          #
# //  taban bölme      #
########################
print('#' * 45)
print(2 + 3, 2.3 + 3.2)
print(2 - 3, 9.3 - 1.2)
print(2 * 3, 92.63 * 2.8)
print(2 / 3, 8.4 / 2.2)
print(2 ** 3)
print(4 ** 0.5) #bir sayının 0.5'inci kuvveti, o sayının kareköküdür.
print("Python" + "Programlama") #buradaki + işleci toplama yerine string değerleri birleştirme işlemi yapıyor. 
print(4 % 3) #kalanı verir.
print(9 // 2) #tam bölme işlemi yapar.
print('#' * 45) #buradaki * işleci çarpma yerine string değeri verilen sayı kadar tekrarlama işlemi yapıyor. 

#############################
# 2.Karşılaştırma İşleçleri #
# ==    eşittir             #
# !=    eşit değildir       #
# >     büyüktür            #
# <     küçüktür            #
# >=    büyük veva eşittir  #
# <=    küçük veya eşittir  #
#############################

parola = "123"
giris = input("Parolayı Giriniz : ")

if parola == giris:
    print("Girilen Parola Doğru!")
elif parola != giris:
    print("Girilen Parola Yanlış!")
  
  
sayi = input("sayı giriniz : ")

if int(sayi) <= 100:
    print("sayı 100 veya 100'den küçük")
elif int(sayi) >= 100:
    print("sayı 100 veya 100'den büyük")
    
print('#' * 45)

########################
### 3.Bool İşleçleri ###
### and    ve        ###
### or     veya      ###
### not    değil     ###
########################

# 1- And 
# True, True => True
# True, False => False
# False, False => False

# 2- Or
# True, True => True
# True, False => True
# False, False => False

# 3- Not
# False => True
# True => False

print(1==1) #True
print(1!=1) #False

print("and :", 'a'=='a' and 5==5) #True
print("and :", 'a'=='a' and 5==-6) #False

print("or :", 'a'=='a' or 45==5) #True
print("or :", 'a'=='ab' or 5==-6) #False

print("not :", not 5==5) #False
print("not :", not 5!=5) #True

print(bool(3)) #True
print(bool("py")) #True
print(bool(" ")) #True
print(bool("    ")) #True
print(bool("0")) #True (0’ın bir sayı, “0”’ın ise bir karakter dizisidir. Sayı olan 0’ın bool değeri False’tur, ama karakter dizisi olan “0”’ın değeri True’dur)
print(bool(0)) #False
print(bool("")) #False


parola = ""
print(bool(parola)) #False
print(not parola) #True

parola = "123"
print(bool(parola)) #True
print(not parola) #False
print('#' * 45)

###########################
# 4.Değer Atama İşleçleri #
# =     atama işleci      #
# +=    topla ata         #
# -=    çıkar ata         #
# *=    çarp ata          #
# /=    böl ata           #
# %=    modülüs ata       #
# **=   kuvvet ata        #
# //=   taban böl ata     #
# :=    walrus operatörü  #
###########################

a = 13

a += 5 #a = a + 5 işlemiyle aynı işi yapar.
a -= 5
a *= 2 #a = a * 2
a /= 2
a %= 5 #a = a % 5
a **= 2
a //= 2 #a = a // 2
print("Değer Atama İşleçleri :", a) #4

#
giris = len(input("Adın ne? "))
if giris < 4:
    print("Adın kısaymış.")
elif giris < 6:
    print("Adın biraz uzunmuş.")
else:
    print("Çok uzun bir adın var.")
    
#walrus operatörü ile
if (giris := len(input("Adın ne? "))) < 4:
    print("Adın kısaymış.")
elif giris < 6:
    print("Adın biraz uzunmuş.")
else:
    print("Çok uzun bir adın var.")

print('#' * 45)

################################
# 5.Bitwise (Bitsel) İşleçleri #
# &     Mantıksal And          #
# |     Mantıksal Or           #
# ^     Mantıksal XOR          #
# >>    Kaydırma               #
# <<    Kaydırma               #
# ~     Tümleme                #
################################
'''
And işlemi ile karşılaştırılmış iki bitten biri bile 0 olsa; 0 sonucunu alırsınız. 1 sonucu alabilmek için her iki bitin de 1 olması gerek.
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0
'''
a = 10                   # 0000 1010 = 10
b = 20                   # 0001 0100 = 20
print("AND :", a & b)    # 0000 0000 = 0

print("AND :", 15 & 11)  # 0000 1111 = 15
                         # 0000 1011 = 11
                         # 0000 1011 = 11
'''
Or işlemi ile karşılaştırılmış iki bitten sadece biri bile 1 olsa; 1 sonucunu alırsınız. 0 sonucu alabilmek için her iki bitin de 0 olması gerek.
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0
'''
a = 10                  # 0000 1010 = 10
b = 20                  # 0001 0100 = 20
print("OR :", a | b)    # 0001 1110 = 30

print("OR :", 15 | 11)  # 0000 1111 = 15
                        # 0000 1011 = 11
                        # 0000 1111 = 15
'''
XOR (ya da) ile karşılaştırma işleminin 1 (doğru) olabilmesi için önermelerin birbirinden farklı doğruluk değerlerine sahip olması gerekmektedir.
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 1 = 1
0 ^ 0 = 0
'''
a = 10                  # 0000 1010 = 10
b = 20                  # 0001 0100 = 20
print("XOR :", a ^ b)   # 0001 1110 = 30

print("XOR :", 15 ^ 11) # 0000 1111 = 15
                        # 0000 1011 = 11
                        # 0000 0100 = 4
'''
Tümleme (Invert) İşleci (~)
Bu işlecin görevi aldığı değeri tersine çevirmektir.
~1 = 0
~0 = 1
'''
a = 1                   # 0000 0001 = 1
print("Tümleme :", ~a)  # 1111 1110 = -2

b = 19                  # 0001 0011 = 19
print("Tümleme :", ~b)  # 1110 1100 = -20

'''
Shifting (kaydırma) İşleçleri (`>>` `<<`)
'''
a = 64                     # 0100 0000 = 64
print("Kaydırma :", a >> 3)# 0000 1000 = 8

b = 16                     # 0001 0000 = 16
print("Kaydırma :", b << 2)# 0100 0000 = 64

a = 15                     # 0000 1111 = 15
print("Kaydırma :", a >> 3)# 0000 0001 = 1
print('#' * 45)

##########################
### 6.Aitlik İşleçleri ###
# in    aitlik işleci    #
##########################
a = "abcd"
print("a" in a) #True

print("f" in a) #False
print('#' * 45)

##########################
### 7.Kimlik İşleçleri ###
# id() identity (kimlik) #
# is   karşılaştırma     #
##########################

a = 100
print("id :", id(a)) #137990748

k = "Dünya!"
print("id :", id(k)) #14461728


a = 256
print(a is 256) #True

a = 257
print(a is 257) #False

a = -5
print(a is -5) #True

a = -6
print(a is -6) #False
print('#' * 45)