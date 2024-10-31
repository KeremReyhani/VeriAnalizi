import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


np.random.seed(0)   # random fonksiyonunda her zaman aynı veri setini üretir
veri=np.random.normal(35,2,40000)
veriz=(veri-np.mean(veri))/np.std(veri)
sns.displot(veriz,kde=True)
plt.title("Veri Dağılım Grafiği",fontsize=15,loc="right",c="red")
plt.xlabel("Veriler",fontsize=15,c="red")
plt.ylabel("Frekans",fontsize=15,c="red")
plt.xlim(-3,3)
plt.axvline(x=np.mean(veriz),linestyle="--",linewidth=2.5,label="Ortalama",c="red")
plt.axvline(x=np.mean(veriz)-np.std(veriz),linestyle="--",linewidth=2.5,label="1 Standart Sapma",c="black")
plt.axvline(x=np.mean(veriz)+np.std(veriz),linestyle="--",linewidth=2.5,c="black")
plt.axvline(x=np.mean(veriz)-2*np.std(veriz),linestyle="--",linewidth=2.5,label="2 Standart Sapma",c="grey")
plt.axvline(x=np.mean(veriz)+2*np.std(veriz),linestyle="--",linewidth=2.5,c="grey")
plt.legend()
plt.show()