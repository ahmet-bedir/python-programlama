### Tam Sayıların Metotları
metot = [i for i in dir(int) if not i.startswith("_")]
print(metot)

# bit_length() metodu herhangi bir tam sayının kaç bit’lik bir yer kapladığını öğrenmek için kullanılır.
for i in range(11):
    print(i, bin(i)[2:], str(len(bin(i)[2:])) + " bitlik.", sep="\t")
    
    
#
sayi = 10
print(f"{sayi} sayısı {sayi.bit_length()} bitlik bir yer kaplamaktadır.")