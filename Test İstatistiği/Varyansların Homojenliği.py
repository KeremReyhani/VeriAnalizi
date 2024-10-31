from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""np.random.seed(0)

x1=stats.norm.rvs(loc=0,scale=1,size=1000)
x2=stats.norm.rvs(loc=0,scale=5,size=1000)
x3=stats.norm.rvs(loc=0,scale=10,size=1000)

sns.set_theme()

sns.kdeplot(x1,label="x1")
sns.kdeplot(x2,label="x2")
sns.kdeplot(x3,label="x3")

plt.legend(loc="upper right")
plt.show()"""





x1=stats.norm.rvs(loc=0,scale=1,size=1000)
x11=np.random.choice(x1,size=750)
x12=np.random.choice(x1,size=250)

x1var=np.var(x1)
x11var=np.var(x1)
x12var=np.var(x12)

sns.set_theme()

sns.kdeplot(x1,label="x1 "+str(x1var))
sns.kdeplot(x11,label="x11 "+str(x11var))
sns.kdeplot(x12,label="x12 "+str(x12var))

plt.legend(loc="upper right")
plt.show()