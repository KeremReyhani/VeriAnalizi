# T dağılımı ortalama güven aralığı, standart sapmanın
# bilinmediği durumlarda kullanılır.

import numpy as np
from scipy import stats

n=30
ortalama=140
sapma=25
guven=0.95
serbestlik=n-1

aralık=stats.t.interval(guven,loc=ortalama,df=serbestlik,scale=sapma/np.sqrt(n))
print(aralık)