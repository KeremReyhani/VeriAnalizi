# aynı bireylerden ya da deneklerden birden fazla ölçüm alındığında
# kullanılan bir istatistiksel testtir. Bu analiz, farklı zaman noktalarında
# ya da farklı koşullar altında alınan ölçümlerdeki değişiklikleri incelemek
# için kullanılır.

import pandas as pd
import pingouin as pg

veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Test İstatistiği/örneklem.xlsx")

veri2=pd.melt(veri,id_vars=["Örneklem"],value_vars=["TÖ","TS1","TS2","TS3"])
veri2.columns=["Örneklem","Testler","Puanlar"]
#print(veri2)

normallik=pg.normality(data=veri2,dv="Puanlar",group="Testler",method="shapiro")
#print(normallik)

homojenlik=pg.sphericity(data=veri2,dv="Puanlar",subject="Örneklem",within="Testler")
#print(homojenlik)

anova=pg.rm_anova(data=veri2,dv="Puanlar",subject="Örneklem",within="Testler")
#print(anova)

posthoc=pg.pairwise_tests(data=veri2,dv="Puanlar",subject="Örneklem",within="Testler",padjust="bonf")
print(posthoc)

