import pandas as pd
import numpy as np

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])   #(data, indexes, panda series)        
bool_df = df > 0
#print(bool_df)
#print(df[bool_df])

#print(df['W'] > 0)
#print(df[['W','X']] > 0)
#print(df[df['W'] > 0])
#print(df[df['Z'] < 0])

resultdf = df[df['W'] > 0]
#print(resultdf['X'])
#print(df[df['W'] > 0]['X'])
#print(df[df['W'] > 0][['X','Y']])


boolser = df['W']>0
result = df[boolser]
mycols = ['Y','X']
#print(result[mycols])


#print(df[(df['W'] > 0) & (df['Y'] > 1)])
#print(df[(df['W'] > 0) | (df['Y'] > 1)])


#print(df.loc[['A'],['W']])


#df = df.reset_index()
#print(df)


newind = 'CA NY WY OR CO'.split()
df['States'] = newind
#print(df)

df=df.set_index('States')
#print(df)






























