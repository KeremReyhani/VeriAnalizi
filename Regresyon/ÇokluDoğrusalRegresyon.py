import pandas as pd
import statsmodels.api as sm

veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Regresyon/çoklu.xlsx")

x=veri[["TavukFiyat","Gelir","SığırFiyat"]]
y=veri["TavukTüketim"]

sabit=sm.add_constant(x)
model=sm.OLS(y,sabit).fit()
print(model.summary())