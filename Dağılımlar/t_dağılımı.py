# serbestlik derecesi artarsa normal dağılıma yaklaşır

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
veri1t=stats.t.rvs(loc=0,df=1,size=15)  # loc: ortalama  df: standart sapma
veri2t=stats.t.rvs(loc=0,df=2,size=15)
veri3t=stats.t.rvs(loc=0,df=5,size=15)
veri4t=stats.t.rvs(loc=0,df=15,size=15)


plt.xlim(-5,5)
sns.distplot(veri1t,color="red")
sns.distplot(veri2t,color="blue")
sns.distplot(veri3t,color="green")
sns.distplot(veri4t,color="yellow")
plt.show()