import numpy as np
arr = np.arange(0,11)
#print(arr[1:5])


arr[0:5] = 100
#print(arr)

arr = np.arange(0,11)
slice_of_arr = arr[0:6]
#print(slice_of_arr)
slice_of_arr[:] = 99
#print(slice_of_arr)
#print(arr)          # changed the values in the original array too because of the reference of the slice_of_arr and arr


arr_copy = arr.copy()
#print(arr_copy)
arr_copy[:] = 1000
#print(arr_copy)    # did not change the values in the original array
#print(arr)


arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
#print(arr_2d)


#print(arr_2d[0][1])
#print(arr_2d[0,1])
#print(arr_2d[:2,1:])




arr = np.arange(0,11)
bool_arr = arr > 5
#print(bool_arr)
#print(arr[bool_arr])

ar = arr[arr>5]
#print(ar)













