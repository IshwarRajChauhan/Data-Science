import pandas as pd
import numpy as np

labels = ['a','b','c']
my_data = [10,20,30]
a = np.array(my_data)
d = {'a':10,'b':20,'c':30}

arr = pd.Series(data=my_data,index=labels)
#print(arr)

arr = pd.Series(my_data,labels)
#print(arr)

arr = pd.Series(a,labels)
#print(arr)

arr = pd.Series(d)
#print(arr)

arr = pd.Series(data = labels)
#print(arr)


arr = pd.Series(data=[sum,print,len])
#print(arr)


ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
#print(ser1)
ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
#print(ser2)
#print(ser1['USA'])
ser3 = pd.Series(data=ser1.values, index=ser2.index)
#print(ser3)

#print(ser1+ser2)




















