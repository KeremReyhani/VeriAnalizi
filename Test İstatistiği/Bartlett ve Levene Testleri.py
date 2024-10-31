# varyansların eşitliğini değerlendirmek için kullanılır
import pandas as pd
from scipy import stats

veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Test İstatistiği/veri.xlsx")

erkek=veri[veri["Cinsiyet"]=="Erkek"]
kadin=veri[veri["Cinsiyet"]=="Kadın"]

"""p1=stats.shapiro(erkek["Harcama"])
p2=stats.shapiro(kadin["Harcama"])
print(p1)
print(p2)"""

h1=stats.levene(erkek["Harcama"],kadin["Harcama"],center="mean")
h2=stats.bartlett(erkek["Harcama"],kadin["Harcama"])

print(h1)
print(h2)

