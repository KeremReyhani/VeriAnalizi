import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.neighbors import LocalOutlierFactor

"""yas=[30,32,33,30,32,35,32,31,30,110]

sns.boxplot(data=yas)
plt.show()"""



"""yas=[30,33,31,33,30]
yıl=[7,10,9,12,25]

sns.scatterplot(x=yas,y=yıl)
plt.show()"""




"""veri=sns.load_dataset("titanic")
veri2=veri.copy()"""

#print(veri2.isnull().sum())

#veri2["age"].fillna(veri2.groupby("sex")["age"].transform("mean"),inplace=True)
#print(veri2.isnull().sum())

"""sns.boxplot(data=veri2["age"])
plt.show()"""

"""Q1=veri2["age"].quantile(0.25)
Q3=veri2["age"].quantile(0.75)
IQR=Q3-Q1

altsınır=Q1-1.5*IQR
ustsınır=Q3+1.5*IQR

askucuk=veri2[veri2["age"]<altsınır]["age"]
#print(askucuk)

usbuyuk=veri2[veri2["age"]>altsınır]["age"]
#print(usbuyuk)"""





"""veri=sns.load_dataset("taxis")
veri2=veri.copy()"""

"""sns.scatterplot(data=veri2,x="fare",y="tip")
plt.show()"""

"""aykırı=pd.DataFrame(data=veri,columns=["fare","tip"])
#print(aykırı)

LOF=LocalOutlierFactor(n_neighbors=20,contamination=0.1)
tahmin=LOF.fit_predict(aykırı)
print(aykırı[tahmin==-1])"""






veri=sns.load_dataset("taxis")
veri2=veri.copy()

"""sns.boxplot(data=veri2["tip"])
plt.show()"""

q1=veri2["tip"].quantile(0.25)
q3=veri2["tip"].quantile(0.75)
IQR=q3-q1

altsınır=q1-1.5*IQR
ustsınır=q3+1.5*IQR

aykırımin=veri2[veri2["tip"]<altsınır]["tip"]
aykırımax=veri2[veri2["tip"]>ustsınır]["tip"]

aykırı=pd.concat([aykırımin,aykırımax],axis=0).index
#print(aykırı)

indeksler=[]

for i in aykırı:
    indeksler.append(i)

#print(indeksler)

"""veri3=veri2.drop(veri2.index[indeksler])
#print(veri2)
#print(veri3)

sns.boxplot(data=veri3["tip"])
plt.show()"""


"""ortalama=veri["tip"].mean()
#print(ortalama)

veri2.loc[indeksler,"tip"]=ortalama
print(veri2["tip"][indeksler])
sns.boxplot(data=veri2["tip"])
plt.show()"""


veri2.loc[veri2["tip"]<altsınır,"tip"]=altsınır
veri2.loc[veri2["tip"]>ustsınır,"tip"]=ustsınır
sns.boxplot(data=veri2["tip"])
plt.show()