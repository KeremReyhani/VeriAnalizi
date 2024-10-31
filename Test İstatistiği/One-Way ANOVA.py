# gruplar arasındaki ortalama farkların anlamlı olup
# olmadığını test etmek için kullanılan bir istatistiksel yöntemdir.

from scipy import stats
import pandas as pd

"""grupA=[1,2,3,6]
grupB=[1,3,5,7]
grupC=[2,4,6,8]

Fdeger,Pdeger=stats.f_oneway(grupA,grupB,grupC)
print(Fdeger,Pdeger)"""







veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Test İstatistiği/anova.xlsx")

g1=veri[veri["Eğitim"]=="İlkokul"]
g2=veri[veri["Eğitim"]=="Lise"]
g3=veri[veri["Eğitim"]=="Üniversite"]
g4=veri[veri["Eğitim"]=="YüksekLisans"]

"""normallik=stats.shapiro(g1["Tvizleme"])
print(normallik)"""

"""homojenlik=stats.bartlett(g1["Tvizleme"],g2["Tvizleme"],g3["Tvizleme"],g4["Tvizleme"])
print(homojenlik)"""

testanova=stats.f_oneway(g1["Tvizleme"],g2["Tvizleme"],g3["Tvizleme"],g4["Tvizleme"])
print(testanova)  # pvalue 0.05ten küçük ortalamalar arasında fark var