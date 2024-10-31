# iki sonucu olan olaylarda kullanılır p^x.(1-p)^(1-x)

from scipy import stats


# yazı-tura
p=0.5
dagilim=stats.bernoulli(p)

t_olasilik=dagilim.pmf(k=0) #pmf: kütle dağılımı kesikli
y_olasilik=dagilim.pmf(k=1)

print("Yazı Olasılığı: {}, Tura olasılığı: {}".format(y_olasilik,t_olasilik))
print(dagilim.expect())   #beklenen değer