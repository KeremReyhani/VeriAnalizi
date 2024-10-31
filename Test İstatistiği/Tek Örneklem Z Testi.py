# örneklem grubunun ortalamasının karşılaştırılması

from statsmodels.stats.weightstats import ztest

veri=[95,70,120,65,130,38,110,90,60]
alfa=0.05

zhesap,p=ztest(veri,value=80,alternative="larger")
print(zhesap,p)

if p<alfa:
    print("H0 Reddedilir")
else:
    print("H0 reddedilemez")