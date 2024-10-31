from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

"""
# ortalama:15   varyans:9    11'den küçük olma olasılığı

olasilik=stats.norm.pdf(x=11,loc=15,scale=3) #pdf: olasılık yoğunluk fonksiyonu: fonksiyonun o noktadaki değeri
print(olasilik)

olasilik2=stats.norm.cdf(x=11,loc=15,scale=3) #cdf: birikimli dağılım fonksiyonu: alan hesabı 
print(olasilik2)"""




x=[0,1,2,3]
p=[1/8,3/8,3/8,1/8]

cum=[]
for i in range(0,len(p)):
    if len(cum)==0:
        cum.append(p[0])
    else:
        cum.append(p[i]+cum[i-1])
print(cum)


plt.bar(x,p)
plt.show()
plt.plot(x,cum,drawstyle="steps")
plt.show()