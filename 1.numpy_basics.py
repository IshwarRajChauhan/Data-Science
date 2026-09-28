import numpy as np
my_list = [1,2,3]
arr = np.array(my_list)
#print(arr)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
arr = np.array(my_mat)
#print(arr)

arr = np.arange(0,11,2)
#print(arr)

arr = np.zeros(3)
#print(arr)

arr = np.zeros((2,5))
#print(arr)

arr = np.ones(3)
#print(arr)

arr = np.ones((2,5))
#print(arr)

arr = np.linspace(0, 5, 100)
#print(arr)


arr = np.eye(4)
#print(arr)


arr = np.random.rand(5)
#print(arr)


arr = arr = np.random.rand(5,5)
#print(arr)


arr = np.random.randn(2)
#print(arr)

arr = np.random.randn(4,4)
#print(arr)


arr = np.random.randint(1, 100,10)
#print(arr)

arr = np.arange(0,25)
#arr = arr.reshape(5, 5)
#print(arr)


a = arr.max()
#print(a)

a = arr.min()
#print(a)


a = arr.argmax()
#print(a)

a = arr.argmin()
#print(a)

a = arr.shape
#print(a)


a = arr.reshape(5,5)
#print(a)


a = arr.dtype
print(a)












