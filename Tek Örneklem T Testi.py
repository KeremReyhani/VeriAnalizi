#  bir veri kümesinin ortalamasının bilinen bir sabit değere eşit olup olmadığını test etmek için kullanılan istatistiksel bir testtir.

from scipy import stats
import pandas as pd

veri=[28,29,35,37,32,26,37,39,22,29,36,38]
alfa=0.05

thesap,p=stats.ttest_1samp(veri,popmean=28,alternative="two-sided") #popmean bilinen ortalama
print(thesap,p)

if p<alfa:
    print("H0 Reddedilir")
else:
    print("H0 Reddedilemez")
