import pandas as pd
import matplotlib.pyplot as plt

veri=pd.DataFrame(pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Betimsel İstatistik Borsa/BIST100.xlsx",usecols=["Bist Getiri"]))
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
#print(veri.describe())
#print(veri.quantile(q=0.25)) #kartil  q parametresi hangi kartilin getirileceği
#print(veri.kurtosis())
#print(veri.skew())



plt.figure()
plt.title("Bist Getiri Dağılımı")
plt.hist(veri["Bist Getiri"],color="g",bins=300,histtype="bar")
plt.show()