import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

veri=sns.load_dataset("tips")

"""sns.regplot(x=veri["total_bill"],y=veri["tip"],ci=None)
plt.show()"""

sabit=sm.add_constant(veri["total_bill"])
bagımlıdeg=veri["tip"]

model=sm.OLS(bagımlıdeg,sabit).fit()
print(model.summary())
print(model.params)

GKT=model.ess+model.ssr
print(GKT)
HKT=model.ssr
print(HKT)
print(1-(HKT/GKT))