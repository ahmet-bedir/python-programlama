#
import os

if os.name == 'posix':
	print('Hoşgeldin Linux Kullanıcısı!')
elif os.name == 'nt':
	print('Hoşgeldin Linux Kullanıcısı!')


# o anda hangi dizin altında bulunduğunuzu öğrenmek için:
print(os.getcwd())

# o anda içinde bulunduğunuz dizinde yeni bir dizin oluşturmak için:
#print(os.makedirs('DATA'))

### subprocess modülü, harici komutları Python içinden çalıştırabilmemizi sağlayan bir araçtır.
import subprocess as sp
sp.call(['bash','komut.sh'])
