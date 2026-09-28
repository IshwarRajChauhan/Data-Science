import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

#----------------------------------------------------------

# sns.lmplot(x="total_bill", y="tip", data=tips,hue="sex")
# sns.lmplot(x="total_bill", y="tip", data=tips,hue="sex",markers=["o", "x"], palette="Set1", height=6, aspect=1.5)
# sns.lmplot(x="total_bill", y="tip", data=tips,hue="sex",markers=["o", "x"], palette="Set1", scatter_kws={"s": 100}, height=6, aspect=1.5)
# sns.lmplot(x="total_bill", y="tip", data=tips,col="day",row='time',hue='sex')
sns.lmplot(x="total_bill", y="tip", data=tips,col="day",row='time',hue='sex',
           aspect=0.6, height=5)


plt.show()
















