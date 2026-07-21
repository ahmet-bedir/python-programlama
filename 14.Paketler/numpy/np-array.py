import numpy as np

# array_list = np.array([1, 2, 3, 4, 5, True, False, 7.7])
# array_list += 1

# print(array_list)
# print(type(array_list))
# print(np.__version__)

###
array0 = np.array(9)  # 0D - Scalar (sıfır boyutlu)
print(array0)
print(f"Kaç boyutlu? {array0.ndim}")

array1 = np.array([23,45,43,26])  # 1D (tek boyutlu array)
print(array1)
print(f"Kaç boyutlu? {array1.ndim}")

array2 = np.array([
    [9,2,5],
    [8,3,2]])  # 2D (iki boyutlu array)
print(array2)
print(f"Kaç boyutlu? {array2.ndim}")

array3 = np.array([
    [[9,2,5],[8,3,2]],
    [[7,3,4],[2,5,3]],
    [[3,6,9],[1,4,5]]
    ])  # 3D (üç boyutlu array)
print(array3)
print(f"Kaç boyutlu? {array3.ndim}")