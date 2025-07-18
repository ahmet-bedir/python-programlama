with open("bilgi iletişim teknolojileri.txt","rb") as file:
    print(file.read(7))
    
    
#
with open("bilgi iletişim teknolojileri.txt","rb") as file:
    okunan = file.read()
    producer_index = okunan.index(b"/Producer")
    print(producer_index)
    print(okunan[14407:14419])