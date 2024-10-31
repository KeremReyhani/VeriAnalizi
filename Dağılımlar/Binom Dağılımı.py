# n denemede iki olası sonucu olan olaylar  (n).p^x.(1-p)^(n-x)
#                                           (x)

from scipy import stats

# 7 defa havaya atılan paranın 3 defa yazı gelme olasılığı

"""p=0.5
n=7

dagilim=stats.binom(n,p)
yazi=dagilim.pmf(k=3)

print(yazi)"""



# 100 üründen 1i kusurlu 10 tane ürünün hepsinin kusursuz olma veya
# max 2 tanesinin kusurlu olma olasılığı

p=0.01
n=10
dagilim=stats.binom(n,p)
ürün0=dagilim.pmf(k=0)
ürün1=dagilim.pmf(k=1)
ürün2=dagilim.pmf(k=2)

toplam=dagilim.cdf(2) #diğer çözüm yolu

print(ürün0+ürün1+ürün2)
print(toplam)

