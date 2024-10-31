import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""hamveri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Veri Ön İşleme/veri.xlsx")
hamveri.to_csv("C:/Users/kerem/Desktop/Programlama/Python/Veri/Veri Ön İşleme/veri.csv")   #csv dosyası daha hızlı okunur
"""

pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)

hamveri=pd.read_csv("C:/Users/kerem/Desktop/Programlama/Python/Veri/Veri Ön İşleme/veri.csv")
veri=hamveri.copy()
#print(veri)

veri.drop(veri.columns[[0]],axis=1,inplace=True)
#print(veri.head())
veri.rename(columns={"Invoice":"Fatura No","StockCode":"Stok Kodu","Description":"Ürün Adı","Quantity":"Adet",
                     "InvoiceDate":"Fatura Tarihi","Price":"Birim Fiyat","Customer ID":"Müşteri ID","Country":"Ülke"},
            inplace="True")
#print(veri)

veri["Toplam Tutar"]=veri["Birim Fiyat"]*veri["Adet"]
#print(veri.head())

#print(veri.info())

veri["Fatura Tarihi"]=pd.to_datetime(veri["Fatura Tarihi"])
#print(veri.info())

veri.drop("Müşteri ID",axis=1,inplace=True)
#print(veri.head())

#print(veri.isnull().sum())

"""veri["Ürün Adı"].fillna(veri["Ürün Adı"].mode()[0],inplace=True)   # eksik değerleri en çok tekrar edenle doldurur
print(veri.isnull().sum())"""

"""oran=(veri["Ürün Adı"].isnull().sum())/len(veri)
print(oran*100)"""

veri.dropna(axis=0,inplace=True)
#print(veri.isnull().sum())
veri.reset_index(drop=True,inplace=True)

iptal=veri[veri["Fatura No"].str.contains("C",na=False)]
#print(iptal)

iptalindeks=[]
for i in iptal.index:
    iptalindeks.append(i)
#print(iptalindeks)

veri.drop(veri.index[iptalindeks],inplace=True)
veri.reset_index(drop=True,inplace=True)
#print(veri)

hata=veri[(veri["Fatura No"].str.len()!=6) | (~veri["Fatura No"].str.isdigit())]   #6 haneden farklı ve sayısal olmayan
#print(hata)

hataindeks=[]
for i in hata.index:
    hataindeks.append(i)
veri.drop(veri.index[hataindeks],inplace=True)
veri.reset_index(drop=True,inplace=True)

hata2=veri[(veri["Stok Kodu"].str.len()!=5) | (~veri["Stok Kodu"].str.isdigit())]
#print(hata2)

hata3=veri[~veri["Stok Kodu"].str.isdigit()]
#print(hata3)

hataindeks2=[]
for i in hata3.index:
    hataindeks2.append(i)
veri.drop(veri.index[hataindeks2],inplace=True)
veri.reset_index(drop=True,inplace=True)

"""print(len(hamveri))
print(len(veri))
print(len(hamveri)-len(veri))"""

hata4=veri[veri["Adet"]<=0]
#print(hata4)
hataindeks3=[]
for i in hata4.index:
    hataindeks3.append(i)
veri.drop(veri.index[hataindeks3],inplace=True)
veri.reset_index(drop=True,inplace=True)

hata5=veri[veri["Birim Fiyat"]<=0]
#print(hata5)
hataindeks4=[]
for i in hata5.index:
    hataindeks4.append(i)
veri.drop(veri.index[hataindeks4],inplace=True)
veri.reset_index(drop=True,inplace=True)


"""sns.boxplot(data=veri,y="Adet")
plt.show()"""

for j in ["Adet","Birim Fiyat","Toplam Tutar"]:
    Q1=veri[j].quantile(0.25)
    Q3=veri[j].quantile(0.75)
    IQR=Q3-Q1

    ustsınır=Q3+1.5*IQR
    altsınır=Q1-1.5*IQR

    aykırı=veri[(veri[j]>ustsınır) | (veri[j]<altsınır)]
    #print(aykırı)

hataindeks5=[]
for i in aykırı.index:
    hataindeks5.append(i)
veri.drop(veri.index[hataindeks5],inplace=True)
veri.reset_index(drop=True,inplace=True)

"""print(len(hamveri))
print(len(veri))
print(len(hamveri)-len(veri))"""

veri=pd.get_dummies(data=veri,columns=["Ülke"],drop_first=True)
#print(veri)
#print(veri.info())

print(veri)