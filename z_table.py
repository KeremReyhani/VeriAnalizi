from scipy.stats import norm


# ortalama = 5.3      standart sapma = 1      P(x<4.5)=?
olasılık=norm(loc=5.3,scale=1).cdf(4.5)
print(olasılık)

# ortalama = 5.3      standart sapma = 1      P(4.5<x<6.5)=?
ustsınır=norm(loc=5.3,scale=1).cdf(6.5)
altsınır=norm(loc=5.3,scale=1).cdf(4.5)
olasılık2=ustsınır-altsınır
print(olasılık2)