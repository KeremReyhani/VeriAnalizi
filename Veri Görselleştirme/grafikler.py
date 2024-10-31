import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

################################## SÜTUN GRAFİK ####################################

"""fiyat=[100,200,250,150]
marka=["A","B","C","D"]

sns.barplot(x=marka,y=fiyat)
plt.show()"""


"""fiyat=[100,200,250,150]
marka=["A","B","C","D"]

fig,ax=plt.subplots(2,2)
ax[1,0].plot(marka,fiyat)
ax[1,1].set_title("Örnek Başlık",color="red")
plt.show()"""


"""fiyat=[100,200,250,150]
marka=["A","B","C","D"]
renkler={"A":"tab:pink",
         "B":"tab:green",
         "C":"tab:orange",
         "D":"tab:red"}
sns.barplot(x=marka,y=fiyat,hue=marka,palette=renkler).set_facecolor("midnightblue")
plt.title("Örnek Başlık",color="darkblue",fontsize=20,fontweight="bold",fontname="Times New Roman",loc="Left",pad=20)
plt.xlabel("Markalar")
plt.xlabel("Fiyatlar")
plt.ylim(0,300)
plt.show()"""




"""fiyat=[100,200,250,150]
marka=["A","B","C","D"]

liste=list(zip(fiyat,marka)) #birleştiriyor
print(liste)

veri=pd.DataFrame(data=liste,columns=["Fiyat","Marka"])
print(veri)

#sns.barplot(x=fiyat,y=marka,orient="h")
sns.barplot(x="Fiyat",y="Marka",data=veri,orient="h",order=veri.sort_values("Fiyat",ascending=False).Marka)
plt.show()"""




################################## ÇİZGİ GRAFİK ####################################

"""tarih=["Ocak","Şubat","Mart","Nisan","Mayıs"]
fiyat=[100,200,150,180,250]

sns.lineplot(x=tarih,y=fiyat,ls="--",marker="o")
plt.grid()
plt.show()"""


"""veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/çizgi.xlsx")

tablo=pd.melt(veri,id_vars="Hafta",value_vars=["HisseA","HisseB","HisseC","HisseD"])
tablo.columns=["Hafta","Hisseler","Fiyatlar"]

sns.lineplot(data=tablo,x="Hafta",y="Fiyatlar",hue="Hisseler",style="Hisseler",markers=True)
plt.show()"""




################################## SAÇILIM GRAFİK ####################################

"""x=[100,200,300,400,500]
y=[150,250,350,450,550]

sns.scatterplot(x=x,y=y)
plt.show()"""


"""veri=sns.load_dataset("tips")

sns.scatterplot(data=veri,x="total_bill",y="tip",hue="day",style="sex")
plt.show()"""






################################## KUTU GRAFİK ####################################

veri=sns.load_dataset("titanic")

özet=veri.describe()
print(özet["age"])

sns.boxplot(x=veri["sex"],y=veri["age"],color="red",showmeans=True)
plt.show()
