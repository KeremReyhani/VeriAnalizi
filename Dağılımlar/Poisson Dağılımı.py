# belli bir zaman dilimi veya bölge için (t^x.e'(-x))/x!

from scipy import stats


# 1dkde 10 adet çağrı geliyor hiç telefon gelmeme olasılığı

ortalama=10
dagilim=stats.poisson(ortalama)
p0=dagilim.pmf(k=0)
print(p0*100)