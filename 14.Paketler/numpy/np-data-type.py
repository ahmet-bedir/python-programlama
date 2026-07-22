import numpy as np

arr = np.array(1)
print(arr.dtype)  # int64 (=8byte) (varsayılan uzunluk)

arr = np.array(1, dtype=np.int8)
print(arr.dtype)  # int8 (=1byte) (uzunluğu kendimiz belirledik)

arr = np.array([1.22,5.38, dtype=np.int8)
print(arr.dtype)  # int8 (=1byte)
