import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('df1.csv',index_col=0)
df2 = pd.read_csv('df2.csv')



# df1['A'].hist(bins=30)
# df1['A'].plot(kind='hist',bins=30)
# df1['A'].plot.hist(bins=30)

#----------------------------------------------

# df2.plot.area()
# df2.plot.bar()
# df2.plot.bar(stacked=True)

#----------------------------------------------

# df1.plot(y='B')
# df1.plot(y='B',figsize=(12,3),lw=1)

#----------------------------------------------

# df1.plot.scatter(x='A',y='B')
# df1.plot.scatter(x='A',y='B',c='C')
# df1.plot.scatter(x='A',y='B',s=df1['C']*100)

#----------------------------------------------

# df2.plot.box()

#----------------------------------------------

# df = pd.DataFrame(np.random.randn(1000,2),columns=['A','B'])
# df.plot.hexbin(x='A',y='B',gridsize=25,cmap='magma',figsize=(12,6))

#----------------------------------------------

# df2['a'].plot.kde()
df2.plot.density()

plt.show()























