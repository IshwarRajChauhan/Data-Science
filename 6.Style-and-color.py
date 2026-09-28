import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")


#----------------------------------------------------------
# plt.figure(figsize=(8, 6))
# sns.set_context('poster')
# sns.set_style("whitegrid")
# sns.countplot(x="sex", data=tips)


#----------------------------------------------------------

sns.lmplot(x="total_bill", y="tip", data=tips,hue='sex', palette='plasma')

plt.show()








