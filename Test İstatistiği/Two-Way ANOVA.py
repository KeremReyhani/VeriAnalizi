import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

veri=pd.read_excel("C:/Users/kerem/Desktop/Programlama/Python/Veri/Test İstatistiği/verim.xlsx")

"""gübrea=veri[veri["Gübre"]=="a"]["Verim"]
gübreb=veri[veri["Gübre"]=="b"]["Verim"]
gübrec=veri[veri["Gübre"]=="c"]["Verim"]

tohumx=veri[veri["Tohum"]=="x"]["Verim"]
tohumy=veri[veri["Tohum"]=="y"]["Verim"]
tohumz=veri[veri["Tohum"]=="z"]["Verim"]
tohumw=veri[veri["Tohum"]=="w"]["Verim"]


normallik=stats.shapiro(gübrec)
print(normallik)
homojenlik=stats.levene(gübrea,gübreb,gübrec)
print(homojenlik)"""



model="Verim ~ C(Gübre) + C(Tohum) + C(Gübre) : C(Tohum)"
test=ols(model,data=veri).fit()
anova=sm.stats.anova_lm(test,type=2)

print(anova)