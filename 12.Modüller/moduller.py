"""
# Modüller
import os

if os.name == 'posix':
	print('Hoşgeldin Linux Kullanıcısı!')
elif os.name == 'nt':
	print('Hoşgeldin Linux Kullanıcısı!')



print(os.getcwd()) # o anda hangi dizin altında bulunduğunuzu öğrenmek için.


print(os.makedirs('DATA')) # o anda içinde bulunduğunuz dizinde yeni bir dizin oluşturmak için.


### subprocess modülü, harici komutları Python içinden çalıştırabilmemizi sağlayan bir araçtır.
import subprocess as sp
sp.call(['bash','komut.sh'])


### webbrowser modülü, bilgisayarımızda kurulu internet tarayıcısını kullanarak internet sitelerini açabilmemizi sağlar.
import webbrowser as web
web.open('www.duckduckgo.com')
"""

### import os gibi bir komutla bütün o isimleri içe aktarmak yerine, yalnızca kullanacağınız isimleri içe aktarmayı tercihde edebilirsiniz. Mesela os modülünün yalnızca name niteliğini kullanacaksanız:
from os import name, listdir
print(name)
#print(getcwd()) #hata!
print(listdir())

