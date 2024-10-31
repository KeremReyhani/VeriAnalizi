import pandas as pd
from numpy import sqrt, log

"""seri1=[1,3,5,7,9]
seri2=[0,2,4,6,8]
baslikliveri=dict(urun1=seri1,urun2=seri2)
veriler=pd.DataFrame(baslikliveri)
print(veriler)"""



"""df=pd.DataFrame([["Elma",10],["Armut",15],["Çilek",20]],columns=["Ürünler","Fiyat"])
print(df) """


"""veri=[["Elma",10],["Armut",15],["Çilek",20]]
baslik=["Ürünler","Fiyat"]
satirno=[1,3,5]
df=pd.DataFrame(veri,columns=baslik,index=satirno)
print(df)"""



"""sozluk={"Ürün":["Elma","Armut","Çilek"],"Fiyat":[10,15,20]}
veri=pd.DataFrame(sozluk)
print(veri)"""


######################## VERİ OKUMA ##########################

"""veri=pd.read_csv("C:/Users/kerem/Desktop/Programlama/Python/Veri/Pandas/USD_TRY Geçmiş Verileri.csv")
print(veri)"""


"""veri=pd.DataFrame(pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Pandas/temelperformans.xlsx"))
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Satırların genişliğini ekran genişliğiyle sınırlama"""

#print(veri)
#print(veri["Kod"])
#print(veri[["Kod","Günlük Getiri (%)"]])
#print(veri.loc[0])
#print(veri.loc[[0,1,2,3,4,5]])
#print(veri.loc[5,"Haftalık Getiri (%)"])
#print(veri.loc[0:5,"Kapanış (TL)":"Aylık Getiri (%)"])



"""veri["Karekök Fiyat"]=sqrt(veri["Kapanış (TL)"])
print(veri)"""

"""veri.insert(2,column="Log Fiyat",value=(log(veri["Kapanış (TL)"])))
print(veri)"""

"""veri2=veri.drop("Yıl İçi Getiri (%)",axis=1)
print(veri2)"""






#print(veri.head())      # ilk beş satır
#print(veri.head(15))
#print(veri.tail())       # son beş satır
#print(veri[5:][["Kod","Kapanış (TL)"]].head(25))


#print(veri=="ACSEL")
#print(veri[veri=="ACSEL"])


#print(veri[veri["Günlük Getiri (%)"]>2])


"""filtre=veri[(veri["Günlük Getiri (%)"]>5)&(veri["Haftalık Getiri (%)"]>7)]
print(filtre)"""





"""veri=pd.DataFrame(pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Pandas/saglik.xlsx"))
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Satırların genişliğini ekran genişliğiyle sınırlama"""
#print(veri)

#print(veri.groupby("İlçe Adı").groups)

"""ilce=veri.groupby("İlçe Adı")
for i in ilce:
    print(i)"""

"""ilce=veri.groupby("İlçe Adı").get_group("BEŞİKTAŞ")
print(ilce)"""





"""veri=pd.DataFrame(pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Pandas/hastane.xlsx"))
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Satırların genişliğini ekran genişliğiyle sınırlama"""
#print(veri)

"""erkek=veri.groupby("Cinsiyet").get_group("Erkek")["Cinsiyet"]
kadin=veri.groupby("Cinsiyet").get_group("Kadın")["Cinsiyet"]
print(erkek.count())
print(kadin.count())"""


"""yasort=veri.groupby("Cinsiyet")["Yas"].mean()
print(yasort)"""

"""yasort=veri.groupby(["Cinsiyet","İl","İlce"])["Yas"].mean()
print(yasort)"""


"""veri2=veri.set_index("Tc")
print(veri2)"""




veri=pd.DataFrame(pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Pandas/hastane - Kopya.xlsx"))
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Satırların genişliğini ekran genişliğiyle sınırlama
#print(veri)
#print(veri.isnull())
#print(veri.isnull().sum())

veri2=veri.dropna(axis=0)  # boş veri olmayanları getirir
print(veri2)
