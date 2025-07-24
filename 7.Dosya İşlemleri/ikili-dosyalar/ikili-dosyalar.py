with open("bilgi-iletisim-teknolojileri.pdf","rb") as file:
    print(file.read(8))
    
    
#PDF dosyasından bilgi alma.
with open("bilgi-iletisim-teknolojileri.pdf","rb") as file:
    okunan = file.read()
    producer_index = okunan.index(b"/Producer")
    
    print(okunan[producer_index:producer_index+80])
    
###  
print('#'*40)
with open("git-commands.pdf","rb") as f:
    okunan = f.read()
    index = okunan.index(b"Type")
    print(okunan[index:index+15])
    
    
###
print('#'*40)
with open("git-commands.html","rb") as f:
    okunan = f.read(52)
    print(okunan)