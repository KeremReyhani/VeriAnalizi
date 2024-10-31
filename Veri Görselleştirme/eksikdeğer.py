import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns

#veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Veri Görselleştirme/eksik.xlsx")
#print(veri.info())

#print(veri.isnull())
#print(veri.isnull().sum())

#print(veri[veri.isnull().any(axis=1)])

#msno.bar(veri)   #eksik verilerin grafiği
#msno.matrix(veri)
#plt.show()




"""veri=sns.load_dataset("titanic")
#print(veri.isnull().sum())

#msno.matrix(veri)
msno.heatmap(veri)
plt.show()"""





"""veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Veri Görselleştirme/eksik.xlsx")
veri2=veri.copy()"""

"""msno.matrix(veri2)
plt.show()"""

"""veri2[~veri2.isnull()]=1
veri2[veri2.isnull()]=0
print(veri2)"""

"""veri3=veri2.notnull().astype("int")
#print(veri3)
print(veri3.corr())"""





veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Veri Görselleştirme/eksik.xlsx")
veri4=veri.copy()

"""veri5=veri4.dropna()
print(veri5)"""

"""veri4.dropna(inplace=True)    # kalıcı siler
veri4.reset_index(drop=True,inplace=True)
print(veri4)"""

#veri4.dropna(inplace=True,how="all")     # bütün değişkenler nan ise siler

"""veri4.fillna(value="Eksik Gözlem",inplace=True)
print(veri4)"""

veri6=veri.copy()
veri6.fillna(value=veri6.mean()["D1":"D2"],inplace=True)
print(veri6)