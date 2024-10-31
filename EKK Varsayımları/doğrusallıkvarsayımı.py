import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import statsmodels.stats.diagnostic as smd

veri=pd.read_csv("C:/Users/kerem/Desktop/Programlama/Python/Veri/EKK Varsayımları/reklam.csv")

####################################### Doğrusallık Varsayımı ###################################
#sns.pairplot(data=veri,y_vars="Sales",x_vars=["TV","Radio","Newspaper"],kind="reg")
#plt.show()

y=veri["Sales"]
x=veri[["TV","Radio","Newspaper"]]

sabit=sm.add_constant(x)
model=sm.OLS(y,sabit).fit()
#print(model.summary())


####################################### Normallik Varsayımı ###################################
#print(model.resid) #hata terimleri
#print(np.mean(model.resid))

#sns.displot(model.resid,kde=True)
#sm.qqplot(model.resid,line="s")
#plt.show()



####################################### Otokorelasyon Varsayımı ###################################
hata=model.resid
sm.graphics.tsa.plot_acf(hata)
#plt.show()

lm=smd.acorr_breusch_godfrey(model,nlags=2)
#print(lm)