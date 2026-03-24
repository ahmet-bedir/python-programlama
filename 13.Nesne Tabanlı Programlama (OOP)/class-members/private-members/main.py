import private

s = private.Sinif()

print(dir(s))

s.ornek_metodu()

'''
Python’da baş tarafında iki adet alt çizgi olan, ancak uç tarafında alt çizgi bulunmayan bütün öğeler birer gizli üyedir. Dışarıya kapalı olan bu gizli üyelere, normal yöntemleri kullanarak sınıf dışından erişemezsiniz.
'''
