import pandas as pd
import numpy as np


data = {'Company' : ['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person' : ['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales' : [200,120,340,124,243,350]
        }

df = pd.DataFrame(data)
#print(df)

byComp = df.groupby('Company')
#print(byComp.mean(numeric_only=True))
#print(byComp.sum())
#print(byComp.std(numeric_only=True))


#print(byComp.sum().loc['FB'])

#print(df.groupby('Company').sum().loc['FB'])

#print(df.groupby('Company').max())

#print(df.groupby('Company').describe())
#print(df.groupby('Company').describe().loc['FB'])

































