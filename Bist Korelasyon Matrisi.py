import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg

hisse=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/matris.xlsx")
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Satırların genişliğini ekran genişliğiyle sınırlama

hissekod=hisse+"."+"IS"

hisseler=hissekod["Kod"].values.tolist()

veri=yf.download(tickers=hisseler,start="2020-01-01",end="2022-05-24")
#print(veri)

fiyat=veri["Adj Close"].reset_index()
#print(fiyat)
#print(fiyat.isna().sum())


getiri=veri["Adj Close"].pct_change()
#print(getiri)

sp=getiri.std()
#print(sp.sort_values(ascending=False))

kor=getiri.corr()

plt.title("Bist30 Getiri Korelasyon Matrisi",color="red",fontsize=15)
sns.heatmap(kor,annot=True,cmap="Blues",xticklabels=True,yticklabels=True)
#plt.show()

anlam=pg.pairwise_corr(getiri)
pd.set_option("display.max_rows",None)
#print(anlam)

print(anlam[anlam["p-unc"]<0.05])