import pandas as pd
import numpy as np

"""veri=pd.DataFrame(pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Pandas/Hastanenorm.xlsx",sheet_name="Doktor"))
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Satırların genişliğini ekran genişliğiyle sınırlama
print(veri)"""


#veri=pd.ExcelFile("C:/Users/kerem/Desktop/Programlama/Python/Veri/Pandas/Hastanenorm.xlsx")
#print(veri.sheet_names)
"""veri2=pd.DataFrame(pd.read_excel(veri,sheet_name=veri.sheet_names[0]))
print(veri2)"""

"""for i in range(0,len(veri.sheet_names)):
    veri2=pd.DataFrame(pd.read_excel(veri,sheet_name=veri.sheet_names[i]))
    print(veri2)"""








"""seri1=pd.DataFrame({
    "Sehir":["Ankara","İstanbul","İzmir","Eskişehir"],
    "Sıcaklık":[15,20,35,30]
})

seri2=pd.DataFrame({
    "Sehir":["Ankara","İstanbul","İzmir","Mersin"],
    "Hava Durumu":["Yağmurlu","Bulutlu","Açık","Kapalı"]
})"""

"""sonuc=pd.merge(seri1,seri2,on="Sehir")   #iki datayı birleştirir
print(sonuc)"""

"""sonuc=pd.merge(seri1,seri2,on="Sehir",how="right")   #iki datayı birleştirir
print(sonuc)"""

"""sonuc=pd.merge(seri1,seri2,on="Sehir",how="left")   #iki datayı birleştirir
print(sonuc)"""

"""sonuc=pd.merge(seri1,seri2,on="Sehir",how="outer")   #iki datayı birleştirir
print(sonuc)"""








"""veri=pd.DataFrame(pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Pandas/hastane.xlsx"))
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)
#veri2=veri.pivot_table(values="Yas",columns="Cinsiyet",aggfunc="sum")
veri2=veri.pivot_table(values="Yas",columns=["Cinsiyet","Kan"],aggfunc="mean",index="İl")
print(veri2)"""




"""seri1=pd.DataFrame({"Ad":["Ali","Veli","Can"],
                    "Soyad":["Aslan","Narlı","Bozgun"]})

seri2=pd.DataFrame({"Sehir":["Ankara","İstanbul","İzmir"],
                    "Sıcaklık":[15,19,25]})

dosya=seri1.to_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Pandas/Bilgiler.xlsx",sheet_name="Ad_Soyad")"""




veri=pd.DataFrame(pd.read_csv("C:/Users/kerem/Desktop/Programlama/Python/Veri/Pandas/araba.csv"))
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)
#print(veri[veri["Km"].max()==veri["Km"]])
print(veri.groupby("Marka")["Fiyat"].mean().sort_values())