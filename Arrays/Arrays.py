import array

# Create an array using array module
my_array = array.array('i') # i for integer, empty array  -----  O(1)
print(my_array)
print(type(my_array))
# minimal contigous block of memory is allocated to the array

my_array1 = array.array('i', [1,2,3,4])     # -----  O(N)
print(my_array1)
# copying elements from list to array
# longer the list, longer time it takes
# Space Complexity is also O(N)


# using numpy array
# import numpy as np

# np_array = np.array([], dtype=int) # empty array  -----  O(1)
# print(np_array)

# np_array1 = np.array([1,2,3,4])     # -----  O(N)
# print(np_array1)

#------------------------------------------------------------------------------------------------
# Insert an element in an array
# at the beginning
my_array1.insert(0,6)    # (index,element) -----   O(n), n-th index will be changed
print(my_array1)
# new element is assigned 0 index
# index of all other elements is shifted
# Time complexity  O(N)
# Space complexity O(1)

# in the middle
my_array1.insert(2,6)      # -----   O(k+m), k and m are no of elements
print(my_array1)

# at the end
my_array1.insert(4,6)
print(my_array1)
# no index needs to be shifted
# if you enter index greater than the array length, 
# the new element will get inserted in the end only


#------------------------------------------------------------------------------------------------
# Array Traversal
