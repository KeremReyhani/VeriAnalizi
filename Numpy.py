import numpy as np

"""
dizi = np.array([1,2,3,4,5,6,7,8])
print(dizi)

print()

dizi2=np.array([[1,2],[3,4],[5,6],[7,8]])
print(dizi2)
print()

print("dizi1'in boyutu: {} ve dizi2'nin boyutu: {}".format(dizi.shape,dizi2.shape))
print()

dizi3=dizi.reshape(2,4)
print(dizi3)
"""

"""
dizi=np.array([1,2,3,4,5],dtype=int)
dizi2=np.array([1,2,3,4,5],dtype=float)
dizi3=np.array([1,2,3,4,5],dtype=complex)
dizi4=np.array([1,2,3,4,5],dtype=str)
dizi5=np.array([1,2,3,4,5],dtype=bool)
print(dizi)
print(dizi2)
print(dizi3)
print(dizi4)
print(dizi5)
"""


"""
sıfır=np.zeros((5,5),dtype=int)
bir=np.ones((3,4),dtype=int)
print(sıfır)
print()
print(bir)
print()
sayi=np.full((4,2),20,dtype=int)
print(sayi)
print()
birim=np.eye(5,dtype=int)
print(birim)
print()
diagonel=np.diag([1,2,3,4,5])
print(diagonel)
print()
artan=np.arange(0,100,5).reshape(4,5)
print(artan)
print()
elemansayi=np.linspace(0,100,5)
print(elemansayi)
print()
rastgele=np.random.randint(0,10,size=(3,4))
print(rastgele)
print()
"""

"""
x=np.array([1,2,3,4,5,6,7,8,9,10])
print(x[0])
print(x[:3])
print(x[::-1])

for i in x:
    print(i)
"""
"""
x=np.array([1,2,3,4,5,6,7,8,9,10]).reshape(5,2)
print(x[0])
print()
print(x[:3])
print()
print(x[::-1])
print()
for i in x:
    print(i)
print()
print(x[:,1])
"""


"""x=np.arange(11)
print(x)
y=np.delete(x,[0,4])
print(y)"""

"""x=np.arange(16).reshape(4,4)
print(x)
print()
y=np.delete(x,[0],axis=0)
print(y)
print()
z=np.delete(x,[0],axis=1)
print(z)"""


"""x=np.arange(9).reshape(3,3)
print(x)
print()
y=np.append(x,[[100,200,300]],axis=0)
print(y)"""

x=np.array([8,6,2,4,5,2])
y=np.array([1,8,9,2,4,4])
print(np.setdiff1d(x,y))
print(np.union1d(x,y))
print(np.isin(x,y))
print(np.unique(x))
print(np.sort(y))