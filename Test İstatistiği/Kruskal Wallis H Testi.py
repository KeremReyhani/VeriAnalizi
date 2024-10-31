# bağımsız gruplar arası medyanların eşitliğine bakar

import pandas as pd
import pingouin as pg
from scikit_posthocs import posthoc_conover

veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Test İstatistiği/yöntem.xlsx")

veri2=pd.melt(veri,value_vars=["A Yöntem","B Yöntem","C Yöntem"])
veri2.columns=["Yöntem","Değer"]

"""normallik=pg.normality(veri2,dv="Değer",group="Yöntem")
print(normallik)"""

"""test=pg.kruskal(veri2,dv="Değer",between="Yöntem")
print(test)"""

posthoc=posthoc_conover(veri2,val_col="Değer",group_col="Yöntem",p_adjust="bonf")
print(posthoc)