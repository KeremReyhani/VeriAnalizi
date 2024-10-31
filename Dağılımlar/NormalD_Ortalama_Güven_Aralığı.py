#Normal dağılım ortalama güven aralığı, örneklem verileri kullanılarak, gerçek ortalamanın hangi aralıkta bulunabileceğini belirler.

import numpy as np
from scipy import stats

# 100 ürün, ortalama ağırlık 1040, standart sapma 25, ortalama ağırlıkları %95 güven ağırlığında kaç?

n=100
x_ort=1040
x_ss=25
guven=0.95

aralık=stats.norm.interval(guven,loc=x_ort,scale=x_ss/np.sqrt(n))
print(aralık)