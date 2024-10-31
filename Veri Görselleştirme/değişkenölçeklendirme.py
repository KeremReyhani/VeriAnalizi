import pandas as pd
import numpy as np
from sklearn import preprocessing as pr
import seaborn as sns

"""veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Veri Görselleştirme/ölçek.xlsx")

maxmindonus=pr.MinMaxScaler().fit_transform(veri)
#print(maxmindonus)

veri2=pd.DataFrame(maxmindonus)
print(veri)
print(veri2)"""






"""veri=sns.load_dataset("titanic")

label=pr.LabelEncoder().fit_transform(veri["sex"])
#print(label)

veri2=pd.DataFrame(label)
#print(veri2)

veri["kodsex"]=veri2
#print(veri[["sex","kodsex"]].head())"""


"""veri=sns.load_dataset("tips")

veri["DayKod"]=pr.LabelEncoder().fit_transform(veri["day"])
print(veri)"""




