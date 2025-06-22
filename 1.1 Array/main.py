from array import array

arr = array('i', [1,2,3,4,5])

# taking array as input
# new_arr = array('i',[])

# n = int(input('Enter length of array'))

# for i in range(n):
#     el = int(input('Enter next element: '))
#     new_arr.append(el)
    
# print(new_arr)

## copy array
copied_array = array(arr.typecode, (e for e in arr))
print(copied_array)