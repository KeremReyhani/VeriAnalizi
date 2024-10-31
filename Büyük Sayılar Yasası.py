#Bu yasa, bir rassal değişkenin beklenen değeri ile ilgili olarak,
# deney sayısı arttıkça (yani, denemeler sayısı sonsuza yaklaştıkça)
# bu değişkenin ortalamasının beklenen değere yakınsaması gerektiğini ifade eder.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

liste=[]
for i in np.arange(0,100):
    deneme=i+1
    yt=np.random.randint(0,2,size=deneme)
    y_olasilik=np.mean(yt)
    liste.append(y_olasilik)

sns.lineplot(data=liste,linewidth=2)
plt.xlabel("Deneme Sayısı")
plt.ylabel("Ortalama")
plt.ylim(0,1)
plt.axhline(0.5,linestyle="--",linewidth=1.5,color="red")
plt.show()