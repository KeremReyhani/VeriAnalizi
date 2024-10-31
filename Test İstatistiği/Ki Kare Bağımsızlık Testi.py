# kategorik iki değişken arasında ilişki var mı yok mu

import pandas as pd
from scipy import stats

veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Test İstatistiği/kikare.xlsx")

tablo=pd.crosstab(index=veri["Cinsiyet"],columns=veri["El"])

"""test,p,sd,beklenen=stats.chi2_contingency(tablo)
print(beklenen)"""


test=stats.fisher_exact(tablo)
print(test)