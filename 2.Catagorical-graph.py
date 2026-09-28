import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')

#------------------------------------------------------------------------------------------

# sns.barplot(x='sex',y='total_bill',data=tips)
# sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)

#------------------------------------------------------------------------------------------

# sns.countplot(x='sex', data=tips)

#------------------------------------------------------------------------------------------


# sns.boxplot(x='day', y='total_bill', data=tips)
# sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')

#------------------------------------------------------------------------------------------

# sns.violinplot(x='day', y='total_bill', data=tips)
# sns.violinplot(x='day', y='total_bill', data=tips, hue='smoker', split=True)


#------------------------------------------------------------------------------------------

# sns.stripplot(x='day', y='total_bill', data=tips , jitter=True , hue='smoker')

#------------------------------------------------------------------------------------------

# sns.swarmplot(x='day', y='total_bill', data=tips,hue='smoker')

#------------------------------------------------------------------------------------------

sns.catplot(x='day', y='total_bill', data=tips, kind='bar')



plt.show()
































