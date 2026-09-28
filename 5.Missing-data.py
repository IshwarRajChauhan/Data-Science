import pandas as pd
import numpy as np


d = {
    'A':[1,2,np.nan],
    'B':[5,np.nan,np.nan],
    'C':[1,2,3]
}

df = pd.DataFrame(d)
#print(df)

#print(df)
#print("-----------------------------")
#print(df.dropna())  #drop rows with missing data
#print("-----------------------------")
#print(df.dropna(axis=1))   #drop columns with missing data

#print(df.dropna(thresh=2))    # atleast two non empty in a row

#print(df.fillna(value="FILL VALUE"))


print(df['A'].fillna(value=df['A'].mean()))




















