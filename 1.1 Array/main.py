from array import array
import numpy as np

arr = array('i', [1,2,3,4,5])

print(type(arr))

# taking array as input
# new_arr = array('i',[])

# n = int(input('Enter length of array'))

# for i in range(n):
#     el = int(input('Enter next element: '))
#     new_arr.append(el)
    
# print(new_arr)

## copy array
# copied_array = array(arr.typecode, (e for e in arr))
# print(copied_array)

# np_arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(np_arr)

linespace = np.linspace(0,12, 10)
# print(linespace)

arg = np.arange(1,10)
# print(arg)

logsp =  np.logspace(1,10,2)
# print('%2.f'%logsp[1])

arr_zaros = np.zeros(5)
# print(arr_zaros)

arr_ones = np.ones(5,'int')
print(arr_ones)