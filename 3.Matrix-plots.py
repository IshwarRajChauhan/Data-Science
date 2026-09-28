import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

#------------------------------------------------------------------------------------------

tc = tips.corr(numeric_only=True)

# sns.heatmap(tc,annot=True)
# sns.heatmap(tc,annot=True,cmap='coolwarm')

#------------------------------------------------------------------------------------------

fp = flights.pivot_table(index='month',columns='year',values='passengers')
# sns.heatmap(fp,cmap='magma')
# sns.heatmap(fp,cmap='magma',linecolor='white',linewidths=1)


#------------------------------------------------------------------------------------------

# sns.clustermap(fp)
sns.clustermap(fp,cmap='coolwarm',standard_scale=1)


plt.show()

























































