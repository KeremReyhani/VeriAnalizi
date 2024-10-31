import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(10)
veri=stats.norm.rvs(loc=38,size=50)

"""sns.distplot(veri)
plt.show()"""

#print(stats.kurtosis(veri))
#print(stats.skew(veri))


"""stats.probplot(veri,dist="norm",plot=plt)
plt.show()"""


"""ks=stats.kstest(veri,cdf="norm",args=(veri.mean(),veri.std())) #standart normal dağılıma uyup uymadığını test eder
print(ks)
print(f"{ks.pvalue:5f}")"""


sw=stats.shapiro(veri)
print(sw)
print(sw.pvalue)