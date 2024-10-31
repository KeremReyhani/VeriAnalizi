import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd

veri=pd.read_csv("C:/Users/kerem/Desktop/Programlama/Python/Veri/EKK Varsayımları/reklam.csv")

y=veri["Sales"]
x=veri[["TV","Radio"]]

sabit=sm.add_constant(x)
model=sm.OLS(y,sabit).fit()
#print(model.summary())

hata=model.resid
whitetest=smd.het_white(hata,model.model.exog)
print(whitetest)

BPtest=smd.het_breuschpagan(hata,model.model.exog)
print(BPtest)
