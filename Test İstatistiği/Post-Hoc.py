# farkın hangi gruplar arasında olduğunu gösterir

from scipy import stats
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pingouin as pg  #varyanslar eşitse
import scikit_posthocs as sp #varyanslar eşit değilse

veri = pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Test İstatistiği/anova.xlsx")

g1=veri[veri["Eğitim"]=="İlkokul"]
g2=veri[veri["Eğitim"]=="Lise"]
g3=veri[veri["Eğitim"]=="Üniversite"]
g4=veri[veri["Eğitim"]=="YüksekLisans"]

"""posthoc=pairwise_tukeyhsd(veri["Tvizleme"],veri["Eğitim"],alpha=0.05)
print(posthoc)


print(g4["Tvizleme"].mean(),g3["Tvizleme"].mean())
print(g4["Tvizleme"].mean(),g1["Tvizleme"].mean())
"""

"""test=pg.welch_anova(data=veri,dv="Tvizleme",between="Eğitim")
print(test)"""

tamhane=sp.posthoc_tamhane(veri,val_col="Tvizleme",group_col="Eğitim")
print(tamhane)