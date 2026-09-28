import pandas as pd
import numpy as np

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])   #(data, indexes, panda series)        
#print(df)
#print(df['W'])
#print(df[['W','Z']])

df['new'] = df['W'] + df['Y']
#print(df)
df.drop('new', axis=1 , inplace=True)   #axis = 1 for columns, 0 for rows
#print(df)

#print(df.drop('E', axis=0, inplace=True))
#print(df)

#print(df.shape)


####### ROWS ########

#print(df.loc['A'])
#print(df.loc[['A','B'],['W','X']])
print(df.iloc[2])










