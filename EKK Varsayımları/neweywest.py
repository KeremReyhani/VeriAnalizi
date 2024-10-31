import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd

veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/EKK Varsayımları/newey-west.xlsx")

y=veri["Y"]
x=veri[["X1","X2","X3"]]

sabit=sm.add_constant(x)
model=sm.OLS(y,sabit).fit()
print(model.summary())

hata=model.resid
sm.graphics.tsa.plot_acf(hata)
#plt.show()

lm=smd.acorr_breusch_godfrey(model,nlags=2)
print(lm)

model2=sm.OLS(y,sabit).fit(cov_type="HAC",cov_kwds={"maxlags":3})
print(model2.summary())