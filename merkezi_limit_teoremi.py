# çekilen örneklem sayısı ne kadar fazla ise normal dağılıma o kadar yaklaşır

import random
import numpy as np
import matplotlib.pyplot as plt

yas=np.random.uniform(low=18,high=75,size=40000)
plt.hist(yas,histtype="bar")
plt.show()
orneklem=[np.mean(random.choices(yas,k=5)) for _ in range(1000)]   # k: örneklem sayısı
plt.hist(orneklem,histtype="bar")
plt.show()
orneklem2=[np.mean(random.choices(yas,k=20)) for _ in range(1000)]
plt.hist(orneklem2,histtype="bar")
plt.show()
orneklem3=[np.mean(random.choices(yas,k=30)) for _ in range(1000)]
plt.hist(orneklem3,histtype="bar")
plt.show()