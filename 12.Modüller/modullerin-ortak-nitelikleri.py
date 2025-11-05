# Modüllerin Özel Nitelikleri
import os, sys, random
set_os = set(dir(os))
set_sys = set(dir(sys))
set_random = set(dir(random))
#print(set_os & set_sys & set_random)
# Bu kodlar, os, sys ve random modüllerinin kesişim kümesini, yani her üç modülde ortak olarak bulunan nitelikleri verecektir:
# {'__doc__', '__package__', '__loader__', '__name__', '__spec__'}

'''
# Zira ‘kodların yeniden kullanılabilir özellikte olması’ (code reusability) programcılıkta aranan bir niteliktir:
moduller = ['os', 'sys', 'random', 'sozluk']
print("Modüller : ", *moduller, sep='  ')

def ortak_nitelikler(moduller):
	kumeler = [set(dir(__import__(modul))) for modul in moduller]
	return set.intersection(*kumeler)

print(ortak_nitelikler(moduller))

### __doc__ Niteliği
import sozluk ; print(sozluk.__doc__)
'''