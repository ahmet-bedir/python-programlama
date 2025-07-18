with open("bilgi-iletisim-teknolojileri.pdf","rb") as file:
    print(file.read(7))
    
    
#PDF dosyasından bilgi alma.
with open("bilgi-iletisim-teknolojileri.pdf","rb") as file:
    okunan = file.read()
    producer_index = okunan.index(b"/Producer")
    
    print(okunan[producer_index:producer_index+80])
