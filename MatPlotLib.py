import matplotlib.pyplot as plt
import numpy as np

"""
seri1=[1,2,3,4,5]
seri2=[10,9,8,7,6]
plt.plot(seri1,seri2)  #ilk parametre x, diğeri y
plt.show()
"""


"""yil=[2015,2016,2017,2018,2019,2020,2021]
fiyat=[100,200,300,400,500,600,700]
plt.plot(yil,fiyat,color="red",linewidth=3,marker=".")
plt.axis([2015,2025,0,1000])  #başlangıç ve bitiş noktaları
plt.title("Fiyat Verileri")
plt.xlabel("Yıl")
plt.ylabel("Fiyat")
plt.show()"""



"""plt.figure() #boş grafik
plt.axis()
plt.title("Örnek Çizgi Grafik")
plt.xlabel("Yillar")
plt.ylabel("Fiyatlar")
x=["2016","2017","2018","2019","2020","2021"]
y=[100,200,300,150,250,350]
z=y-np.mean(y)
plt.plot(x,y,color="red",linewidth=3,marker="o",ms=10,mec="blue",mfc="green",label="Yil")
plt.plot(x,z,linestyle="dotted",label="Fiyat")
plt.legend() #etiketlerin görünmesi
plt.grid() #arka plan
plt.show()"""




"""cs=[1.75,1.5,0.5,3,3.25,2]
puan=[17,15,7,19,20,16]
plt.title("Not Dağılım Grafiği")
plt.xlabel("Saat")
plt.ylabel("Puan")
plt.axis([0,4,0,21])
renkler=np.random.randint(0,100,6)
plt.scatter(cs,puan,s=150,c=renkler,marker="v",cmap="Reds",alpha=0.5)
plt.colorbar()
plt.show()"""





"""x=np.linspace(-10,9,20)
y=x**2
z=x**3
fig=plt.figure()
grafik1=fig.add_axes([0.1,0.1,0.8,0.8])
grafik1.plot(x,y,c="Red")
grafik1.set_xlabel("X Değerleri")
grafik1.set_ylabel("Y Değerleri")
grafik1.set_title("Örnek Grafik")

grafik2=fig.add_axes([0.3,0.6,0.2,0.2])
grafik2.plot(x,z,c="Blue")
grafik2.set_xlabel("X Değerleri")
grafik2.set_ylabel("Z Değerleri")
grafik2.set_title("Örnek Grafik2")
plt.show()"""

"""x=np.linspace(-10,9,20)
y=x**2
z=x**3
fig,grafik=plt.subplots(nrows=2,ncols=1)

grafik[0].plot(x,y)
grafik[0].set_title("1.Grafik")
grafik[1].plot(x,y)
grafik[1].set_title("2.Grafik")
plt.tight_layout()
plt.show()"""





"""araclar=["Fiat","BMW","Ford","Mercedes"]
fiyatlar=[100,200,300,400]
plt.bar(araclar,fiyatlar)
plt.show()"""

"""sınıflar=["A","B","C","D","E"]
indeks=np.arange(len(sınıflar))
a=0.25
matematik=[90,55,75,45,35]
turkce=[80,58,77,90,35]
fizik=[40,35,68,78,80]
plt.bar(indeks-a,matematik,label="Matematik",color="Red",width=a)
plt.bar(indeks,turkce,label="Türkçe",color="Blue",width=a)
plt.bar(indeks+a,fizik,label="Fizik",color="Green",width=a)
plt.title("Sınıflara Göre Ortalama Not Dağılımı")
plt.xlabel("Sınıflar")
plt.legend()
plt.xticks(ticks=indeks,labels=sınıflar)
plt.show()"""



"""x1=np.random.normal(0,1,1000)
x2=np.random.normal(5,2,1000)
x3=np.random.normal(-5,0.7,1000)
plt.hist(x1,alpha=0.5)
plt.hist(x2,alpha=0.5)
plt.hist(x3,alpha=0.5)
plt.show()"""



araclar=["Fiat","BMW","Ford","Mercedes"]
fiyatlar=[100,200,300,400]
aralık=[0.2,0,0.5,0]
plt.pie(fiyatlar,labels=araclar,startangle=90,explode=aralık,shadow=True)
plt.show()