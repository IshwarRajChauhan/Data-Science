import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# print(tips.head())
#------------------------------------------------------------------------------------------

# sns.histplot(tips['total_bill'],kde=True,bins=30)

#------------------------------------------------------------------------------------------

# sns.jointplot(x='total_bill', y='tip', data=tips,kind='hex')
# sns.jointplot(x='total_bill', y='tip', data=tips,kind='reg')
# sns.jointplot(x='total_bill', y='tip', data=tips,kind='kde')
# sns.jointplot(x='total_bill', y='tip', data=tips)

#------------------------------------------------------------------------------------------

# sns.pairplot(tips)
# sns.pairplot(tips, hue='sex',palette='coolwarm')

#------------------------------------------------------------------------------------------

# sns.rugplot(tips['total_bill'])


#------------------------------------------------------------------------------------------

sns.kdeplot(tips['total_bill'])

plt.show()


















